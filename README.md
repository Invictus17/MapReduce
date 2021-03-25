# MapReduce
A MapReduce framework from scratch

## 1) Map phase
![alt text](https://github.com/Invictus17/MapReduce/blob/main/Map%20phase.PNG)

## 2) Reduce phase
![alt text](https://github.com/Invictus17/MapReduce/blob/main/Reduce%20phase.PNG)

## 3) Assumptions
The map function gets an input argument that has the data to be processed & a document id that refers to the document name that the input belongs to. You can see the mapper & reducer functions in example.py to write your own functions.

## 4) Detailed flow of the system:

1)	The master node is spawned which spawns the Key-value store & the Data service using the ip & ports specified in the config by the user.
2)	The Data Service is given the data input location through a command line argument. It creates a specific directory for each mapper in its Mapper store directory & almost equally divides the input data in chunks & stores them in the respective mapper directories. Every chunk is stored in the form documentID_chunkID – this structure allows a mapper to know what document it is processing using the documentID when received from the Data Service.
3)	Then the master node spawns the mappers with an id – the first thing a mapper does is request the Data Service for its data & stores it locally.
4)	The mappers process the data – apply the map function & store the key value pairs to the key-value store and terminate.
5)	The master then gets the total number of keys in the key-value store using a gRPC request. It equally splits the key indexes for each reducer & spawns them.
6)	The first thing a reducer does is get a list of keys from the key-value store & locates its chunk of keys using the indexes received at the time of spawning from the master. For each key, a reducer gets the respective value from the key-value store & stores it applying the reduce function & storing the result in a file locally. Once the data is stored it transfers it to the Data Service to aggregate.

## 5) Limitations:
Currently I’ve kept the maximum number of mappers & reducers to be 30. But to change that only a single argument value needs to be changed so scaling it for more reducers & mappers won’t be an issue.

## 6) Setup needed:
1)	Please install grpc: python -m pip install grpcio
2)	Please install Python3 and have Python3 to be the default interpreter. i.e when python xyz.py is ran it should pick up python3 as the default interpreter. If it’s not you can do that with:
```
$ echo "alias python='python3'" >> .bashrc
$ source .bashrc
```

## 7) How to run:
1)	Place your input files in the ./Input directory.
2)	 Open example.py select the function you want – pas it in as the argument & run. You can define your own mapper & reducer functions.

map-reduce as a library that can be used by other programs to run a map-reduce task.
A user can import this lib and specify the arguments - Where a user should define the map & reduce functions & pass it to the run() function
a.	run_object = mapreduce(num_mappers = 5, num_reducers = 5)
b.	run_object.run(Input_location, mapper_word_count, reduce_word_count)

## 8) Citations:
https://github.com/gooooloo/grpc-file-transfer for some of the data store functions like upload & download.
