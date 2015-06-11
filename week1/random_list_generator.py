from random import randint


def generator(size, max_value):
    sequence = []
    for i in range(0, size):
        sequence.append(randint(0, max_value))
    return sequence
