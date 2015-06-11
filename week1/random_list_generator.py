from random import randint
import time


def generator(size, max_value):
    sequence = []
    for i in range(0, size):
        sequence.append(randint(0, max_value))
    return sequence


def measure_time(function, sequence):
    start = time.time()
    function(sequence)
    end = time.time()
    result = end - start
    print("Time elapsed for {}: {}".format(function, result))
