from key_val_pb2 import *
from key_val_pb2_grpc import *
from concurrent import futures
import grpc
import argparse
import threading
import logging

logging.basicConfig(level=logging.INFO, format="KeyStore" + ": %(message)s")


class keys_store(master_kvServicer):
    def __init__(self):
        self.dict = {}
        self.lock = threading.Lock()

    def store_key(self, request, context):
        self.lock.acquire()
        if not self.dict.get(request.key):
            self.dict[request.key] = [request.value]
        else:
            self.dict[request.key].append(request.value)

        self.lock.release()
        return store_response(ack="Stored key " + request.key)

    def get_key(self, request, context):
        if self.dict.get(request.key):
            return get_key_response(value=self.dict.get(request.key))
        else:
            return get_key_response(value=[])

    def get_all_keys(self, request, context):
        return all_key_response(response=self.dict.keys())

    def get_number_of_keys(self, request, context):
        return key_length_response(key_length=len(self.dict.keys()))


def main(ip, port):
    service = keys_store()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))

    add_master_kvServicer_to_server(service, server)
    server.add_insecure_port(str(ip) + ":" + str(port))

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start data service")
    parser.add_argument('-ip', '--ip', type=str, help='Enter ip of key value service')
    parser.add_argument('-p', '--port', type=str, help='Enter port of key value service')
    args = parser.parse_args()
    logging.info("Launching key-value store")
    main(args.ip, args.port)
