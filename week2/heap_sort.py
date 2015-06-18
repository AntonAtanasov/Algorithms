class Heapsort:
    def __init__(self):
        self.input_list = []
        self.max_value = len(self.input_list) - 1
        self.input_list = [None] + self.input_list

    def __repr__(self):
        return str(self.input_list)

    def swap(self, i, j):
        self.input_list[i],
        self.input_list[j] = self.input_list[j],
        self.input_list[i]

    def check_parent(self, current_index):
        if current_index // 2 == 0:
            return False
        else:
            return self.input_list[current_index] < self.input_list[current_index // 2]

    def check_child(self):
        pass

    def insert(self, number):
        self.input_list.append(number)
        current_index = len(self.input_list) - 1
        while self.check_parent(current_index):
            self.swap(current_index, current_index // 2)
            current_index = current_index // 2

    def heapify(self, end, i):
        l = 2 * i 
        r = 2 * i + 1
        max=i
        if l < end and self.input_list[i] < self.input_list[l]:
            max = l
        if r < end and self.input_list[max] < self.input_list[r]:
            max = r
        if max != i:
            self.swap(i, max)
            self.heapify(end, max)

    def heap_sort(self):
        end = len(self.input_list)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(end, i)
        for i in range(end-1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0)


def main():
    test = Heapsort()
    test.insert(1)
    test.insert(45)
    test.insert(2)
    # test.heap_sort()
    print(test)

if __name__ == '__main__':
    main()
