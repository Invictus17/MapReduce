from socket import *
import argparse
import logging
import marshal
import base64
import types
import json

import grpc
from key_val_pb2_grpc import *
from key_val_pb2 import *

from data_pb2 import *
from data_pb2_grpc import *

logging.basicConfig(level=logging.INFO, format="Reducer" + ": %(message)s")


def get_keys(ip, port):
    with grpc.insecure_channel(ip + ":" + str(port)) as channel:
        stub = master_kvStub(channel)
        response = stub.get_all_keys(all_key_request(key="all keys"))
    return list(response.response)


def upload(write_loc):
    with open(write_loc, 'rb') as f:
        while True:
            piece = f.read(1024)
            if not piece:
                break
            yield reducer_chunk(buffer=piece)


def main(red, startindex, endindex, id, data_store_ip, data_store_port, key_store_ip, key_store_port):
    write_res = {}
    # Deserialize reduce function
    red_bytes = base64.b64decode(red.encode("utf-8"))
    result = marshal.loads(red_bytes)
    red_func = types.FunctionType(result, globals())

    # Get list of keys
    list_keys = get_keys(key_store_ip, key_store_port)

    write_loc = r"Reducer_data/red_" + str(id)

    this_list = None
    startindex = int(startindex)
    if endindex == "last":
        this_list = list_keys[startindex:]
    else:
        endindex = int(endindex)
        this_list = list_keys[startindex:endindex]

    with grpc.insecure_channel(key_store_ip + ":" + str(key_store_port)) as channel:
        stub = master_kvStub(channel)
        for i in range(len(this_list)):
            response = stub.get_key(get_key_request(key=this_list[i]))

            # Get value for this key
            write_res[this_list[i]] = red_func(response.value)

    file_write = open(write_loc, 'w', encoding="utf-8")
    file_write.write(str(write_res))

    with grpc.insecure_channel(data_store_ip + ":" + data_store_port) as channel:
        stub = masterStub(channel)
        response = stub.upload_files(upload(write_loc))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="spawn a reducer")
    parser.add_argument('-f', '--red', type=str, help='Enter the reducer function')
    parser.add_argument('-s', '--startindex', type=str, help='Enter start index')
    parser.add_argument('-e', '--endindex', type=str, help='Enter end index')
    parser.add_argument('-i', '--id', type=str, help='Enter the reducer id')
    parser.add_argument('-dip', '--dip', type=str, help='Enter ip of data service')
    parser.add_argument('-dp', '--dport', type=str, help='Enter port of data service')
    parser.add_argument('-kip', '--kip', type=str, help='Enter ip of key value store')
    parser.add_argument('-kp', '--kport', type=str, help='Enter port of key value store')
    args = parser.parse_args()

    main(args.red, args.startindex, args.endindex, args.id, args.dip, args.dport, args.kip, args.kport)
