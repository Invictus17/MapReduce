import grpc
from data_pb2_grpc import *
from data_pb2 import *
from concurrent import futures
import os
import argparse
import logging
import shutil
import threading

CHUNK_SIZE = 1024

logging.basicConfig(level=logging.INFO, format="DataServer" + ": %(message)s")


def make_chunks(num_mappers, input_location):
    input_docs = os.listdir(input_location)
    curr_mapper_dir = 0
    chunk_size = 300

    for index, document in enumerate(input_docs):
        chunk_count = 0
        input_file_obj = open(input_location + "/" + document, 'r', encoding="utf-8")
        # documentId_fileCounter
        write_file_obj = open(
            r"Data_server_input/mapper_data_" + str(curr_mapper_dir) + "/" + str(index) + "_" + str(chunk_count), 'a',
            encoding="utf-8")

        line_count = 0
        while True:
            if line_count == chunk_size:
                curr_mapper_dir += 1
                curr_mapper_dir %= num_mappers
                write_file_obj.close()
                chunk_count += 1
                line_count = 0
                write_file_obj = open(
                    r"Data_server_input/mapper_data_" + str(curr_mapper_dir) + "/" + str(index) + "_" + str(chunk_count),
                    'a', encoding="utf-8")

            line = input_file_obj.readline()
            if not line:
                write_file_obj.close()
                break
            write_file_obj.write(line)
            line_count += 1
        curr_mapper_dir += 1
        curr_mapper_dir %= num_mappers


def get_chunks(mapper_id):
    data_location = r"Data_server_input/mapper_data_" + str(mapper_id)

    mapper_files = os.listdir(data_location)
    for document in mapper_files:
        with open(data_location + "/" + document, 'rb') as f:
            while True:
                piece = f.read(CHUNK_SIZE)
                if len(piece) == 0:
                    break
                yield chunk(buffer=piece, file_name=document)


def save_to_file(chunks):
    with open("Final_output/output", 'ab') as file:
        for chunk in chunks:
            file.write(chunk.buffer)


class masterserver(masterServicer):
    def __init__(self):
        self.lock = threading.Lock()

    def download_files(self, request, context):
        logging.info("Mapper {} has requested data".format(request.mapper_id))
        return get_chunks(request.mapper_id)

    def upload_files(self, request_iterator, context):
        self.lock.acquire()
        save_to_file(request_iterator)
        self.lock.release()
        return ack(received="OK")


def main(input_location, num_mappers, server_ip, port):
    # Make mapper data dirs
    for i in range(num_mappers):
        os.mkdir("./Data_server_input/mapper_data_" + str(i))

    chunk__line_size = 300
    make_chunks(num_mappers, input_location)

    service = masterserver()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))

    add_masterServicer_to_server(service, server)
    server.add_insecure_port(str(server_ip) + ":" + str(port))

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start data service")
    parser.add_argument('-i', '--inputlocation', type=str, help='Enter input data location')
    parser.add_argument('-m', '--mappers', type=int, help='Enter number of mappers')
    parser.add_argument('-ip', '--ip', type=str, help='Enter ip of data service')
    parser.add_argument('-p', '--port', type=str, help='Enter port of data service')
    args = parser.parse_args()
    logging.info("Launching data store")
    main(args.inputlocation, args.mappers, args.ip, args.port)