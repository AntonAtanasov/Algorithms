class Vector:
    def __init__(self):
        self.vector = [None] * 100

    def __repr__(self):
        return str(self.vector)

    def check_length(self, index):
        if index > len(self.vector):
            self.vector = self.vector + [None] * len(self.vector)

    def insert(self, index, value):
        self.check_length(index)
        self.vector[index:index + 1] = [value]

    def add(self, value):
        self.vector = self.vector + [None] * len(self.vector)
        self.vector[len(self.vector)] = [value]

    def get(self, index):
        return self.vector[index]

    def remove(self, index):
        self.vector.pop(index)

    def pop(self):
        self.vector.pop()

    def size(self):
        counter = 0
        for element in self.vector:
            if element is not None:
                counter += 1
        return counter

    def capacity(self):
        return len(self.counter)


test_v = Vector()
test_v.insert(0, 1)
test_v.insert(1, 2)
test_v.insert(1, 23)
print(test_v)
