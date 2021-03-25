import sys
import subprocess
import marshal
import base64
import logging
import os, shutil
import glob
logging.basicConfig(level=logging.INFO, format="API" + ": %(message)s")


class mapreduce:
    def __init__(self, num_mappers, num_reducers):
        if num_mappers < 1:
            sys.exit("number of mappers cannot be less than 1")
        if num_reducers < 1:
            sys.exit("number of reducers cannot be less than 1")
        self.num_mappers = num_mappers
        self.num_reducers = num_reducers
        # cleanup
        dirs = ['Data_server_input', 'Final_output', 'Mapper_data', 'Reducer_data']
        # citation: https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
        for folder in dirs:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    continue


    def run(self, input_loc, map_fn, reduce_fn):
        # serialize functions
        map_string = marshal.dumps(map_fn.__code__)
        map_base64 = base64.b64encode(map_string).decode("utf-8")
        red_string = marshal.dumps(reduce_fn.__code__)
        red_base64 = base64.b64encode(red_string).decode("utf-8")

        logging.info("Spawning master")
        # Invoke master
        p = subprocess.Popen("python master.py -m " + str(self.num_mappers) + " -r " + str(self.num_reducers)
                             + " -mf " + map_base64 + " -rf " + red_base64 + " -i " + input_loc)
        p.wait()
