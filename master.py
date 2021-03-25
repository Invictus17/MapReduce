import subprocess
import argparse
import time
import grpc
from concurrent import futures
import logging
import os
import json
import shutil
from key_val_pb2 import *
from key_val_pb2_grpc import *
import grpc

logging.basicConfig(level=logging.INFO, format="Master" + ": %(message)s")


def get_keys_from_key_store(ip, port):
    with grpc.insecure_channel(ip + ":" + str(port)) as channel:
        stub = master_kvStub(channel)

        response = stub.get_number_of_keys(key_length_request(get_key="dict len"))
        return int(response.key_length)


def main(input_location, num_mappers, num_reducers, map_func, red_func, config_dict):
    # prepare key val store & mapper processes
    data_store_process = "python data_server.py -i " + str(input_location) + " -m " + str(num_mappers) \
                         + " -ip " + config_dict['data_store_ip'] + " -p " + config_dict['data_store_port']

    key_store_process = "python key_store_server.py -ip " + config_dict['key_store_ip'] + " -p " \
                        + config_dict['key_store_port']

    process_list = [data_store_process, key_store_process]

    for i in range(num_mappers):
        process_list.append("python mapper.py -i " + str(i) + " -f " + map_func + " --dip " +
                            config_dict['data_store_ip'] + " --dport " + config_dict['data_store_port'] +
                            " --kip " + config_dict['key_store_ip'] + " --kport " + config_dict['key_store_port'])

    # invoke mappers
    logging.info("Spawning key-store, data service & mappers")
    processes = [subprocess.Popen(process) for process in process_list]

    while True:
        if len(processes) == 2:
            break
        for index, process in enumerate(processes):
            if process.poll() is not None:
                processes.pop(index)
            else:
                if len(processes) == 2:
                    break
                time.sleep(0.8)

    # At barrier
    logging.info("Mappers have exited")
    logging.info("At barrier")
    # Get number of keys in the store
    keys = get_keys_from_key_store(config_dict['key_store_ip'], config_dict['key_store_port'])

    # prepare reducers
    start_index = 0
    chunk = keys // num_reducers
    end_index = chunk
    reducers_list = []
    for i in range(num_reducers):
        if i == num_reducers - 1:
            reducers_list.append("python reducer.py -s " + str(start_index) + " -e "
                                 + "last" + " -f " + red_func + " -i " + str(i) + " -dip " +
                                 config_dict["data_store_ip"] + " -dp " + config_dict["data_store_port"] + " -kip "
                                 + config_dict["key_store_ip"] + " -kp " + config_dict["key_store_port"])
        else:
            reducers_list.append("python reducer.py -s " + str(start_index) + " -e "
                                 + str(end_index) + " -f " + red_func + " -i " + str(i) + " -dip " +
                                 config_dict["data_store_ip"] + " -dp " + config_dict["data_store_port"] + " -kip "
                                 + config_dict["key_store_ip"] + " -kp " + config_dict["key_store_port"])
        start_index = end_index
        end_index += chunk

    logging.info("Spawning reducers")
    # Invoke reducers
    for process in reducers_list:
        processes.append(subprocess.Popen(process))


    while True:
        if len(processes) == 2:
            break
        for index, process in enumerate(processes):
            if process.poll() is not None:
                processes.pop(index)
            else:
                if len(processes) == 2:
                    break
                time.sleep(0.8)

    logging.info("Reducers have exited")
    processes[0].terminate()
    processes[1].terminate()
    processes.pop()
    processes.pop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the master")
    parser.add_argument('-i', '--inputlocation', type=str, default=1,
                        help='Enter input data location')
    parser.add_argument('-m', '--mappers', type=int, default=1,
                        help='Enter number of mappers')
    parser.add_argument('-r', '--reducers', type=int, default=1,
                        help='Enter number of reducers')
    parser.add_argument('-mf', '--map', type=str, default=None,
                        help='Enter map function')
    parser.add_argument('-rf', '--red', type=str, default=None,
                        help='Enter reduce function')
    args = parser.parse_args()

    with open('./config.json') as config_file:
        config_data = json.load(config_file)

    config_dict = config_data

    main(args.inputlocation, args.mappers, args.reducers, args.map, args.red, config_dict)
