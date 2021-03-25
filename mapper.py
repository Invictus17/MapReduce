import argparse
import marshal
import types
import base64
from socket import *
import logging
import os
import grpc

from key_val_pb2_grpc import master_kvStub as key_stub
from key_val_pb2 import store_request

from data_pb2 import mapper_request
from data_pb2_grpc import masterStub as datamaster_stub

logging.basicConfig(level=logging.INFO, format="mapper" + ": %(message)s")


def send_to_key_val_store(request_list, key_store_ip, key_store_port):
    with grpc.insecure_channel(key_store_ip + ":" + key_store_port) as channel:
        stub = key_stub(channel)
        for key, val in request_list:
            response = stub.store_key(store_request(key=key, value=val))


def main(map_func, id, data_store_ip, data_store_port, key_store_ip, key_store_port):
    data_location = r"./Mapper_data/mapper_data_" + str(id)

    map_bytes = base64.b64decode(map_func.encode("utf-8"))
    result = marshal.loads(map_bytes)
    map_func = types.FunctionType(result, globals())

    # Get all the documents to process from data service
    with grpc.insecure_channel(data_store_ip + ':' + data_store_port) as channel:
        stub = datamaster_stub(channel)
        responses = stub.download_files(mapper_request(mapper_id=id))

        os.mkdir(data_location)
        for response in responses:
            with open(data_location + "/" + response.file_name, 'ab') as file_write:
                file_write.write(response.buffer)

    logging.info("Mapper {} has received all data files to process".format(str(id)))

    for document in os.listdir(data_location):
        doc_id = document.split("_")[0]
        file_obj = open(data_location + "/" + document, 'r', encoding="utf=8")
        res = ""
        while True:
            line = file_obj.readline()
            if not line:
                break
            res += " " + line.strip().lower()

        send_to_key_val_store(map_func(res, doc_id), key_store_ip, key_store_port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="spawn a mapper")
    parser.add_argument('-f', '--map', type=str, help='Enter the map function')
    parser.add_argument('-i', '--id', type=str, help='Enter the mapper id')
    parser.add_argument('-dip', '--dip', type=str, help='Enter ip of data service')
    parser.add_argument('-dp', '--dport', type=str, help='Enter port of data service')
    parser.add_argument('-kip', '--kip', type=str, help='Enter ip of key value store')
    parser.add_argument('-kp', '--kport', type=str, help='Enter port of key value store')
    args = parser.parse_args()

    main(args.map, args.id, args.dip, args.dport, args.kip, args.kport)
