from random_list_generator import generator, measure_time


def selection_sort(sequence):
    for fillslot in range(len(sequence) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if sequence[location] > sequence[positionOfMax]:
                positionOfMax = location

        temp = sequence[fillslot]
        sequence[fillslot] = sequence[positionOfMax]
        sequence[positionOfMax] = temp


def insertion_sort(sequence):
    for index in range(1, len(sequence)):

        currentvalue = sequence[index]
        position = index

        while position > 0 and sequence[position - 1] > currentvalue:
            sequence[position] = sequence[position - 1]
            position = position - 1

        sequence[position] = currentvalue


def quick_sort(sequence):
    if sequence == []:
        return []
    pivot = sequence[0]
    l = quick_sort([x for x in sequence[1:] if x < pivot])
    u = quick_sort([x for x in sequence[1:] if x >= pivot])
    return l + [pivot] + u


test_seq3 = generator(10000, 10000)
test_seq1 = generator(10000, 10000)
test_seq2 = generator(10000, 10000)


measure_time(quick_sort, test_seq3)
measure_time(insertion_sort, test_seq2)
measure_time(selection_sort, test_seq1)
