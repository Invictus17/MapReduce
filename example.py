def mapper_word_count(input, doc_id):
    import string
    input = input.translate(str.maketrans('', '', string.punctuation))
    input = input.split(" ")
    word_op = []

    for word in input:
        if word != "":
            word_op.append((word, 1))

    return word_op


def reducer_word_count(input):
    return sum(input)


def mapper_inverted_index(input, doc_id):
    import string
    input = input.translate(str.maketrans('', '', string.punctuation))
    input = input.split(" ")
    word_op = []

    for word in input:
        if word != "":
            word_op.append((word + "_" + doc_id, 1))

    return word_op


def reducer_inverted_index(input):
    return sum(input)

from mapreduce import mapreduce

input_location = r"./Input"
run_object = mapreduce(num_mappers=5, num_reducers=5)
run_object.run(input_location, mapper_word_count, reducer_word_count)
