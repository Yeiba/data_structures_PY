class MinIndexedBinaryHeap:
    def __init__(self, max_size):
        self.d = 2  # Binary heap
        self.max_size = max_size
        self.size = 0
        self.heap = [None] * max_size
        # Maps indices to their positions in the heap
        self.positions = [-1] * max_size
        self.keys = [None] * max_size

    def add(self, index, key):
        if index < 0 or index >= self.max_size:
            raise IndexError('Index out of bounds')
        if self.positions[index] != -1:
            raise ValueError('Index already in heap')

        self.heap[self.size] = index
        self.keys[index] = key
        self.positions[index] = self.size
        self.size += 1
        self.swim(self.size - 1)

    def remove(self, index):
        if index < 0 or index >= self.max_size or self.positions[index] == -1:
            raise ValueError('Index not in heap')

        heap_index = self.positions[index]
        self.swap(heap_index, self.size - 1)
        self.size -= 1
        self.sink(heap_index)
        self.positions[index] = -1
        self.keys[index] = None

    def peek(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def get_key(self, index):
        if index < 0 or index >= self.max_size:
            raise IndexError('Index out of bounds')
        return self.keys[index]

    def swim(self, i):
        while i > 0 and self.less(i, (i - 1) // self.d):
            parent = (i - 1) // self.d
            self.swap(i, parent)
            i = parent

    def sink(self, i):
        while True:
            smallest = i
            for j in range(self.d * i + 1, min(self.size, self.d * i + self.d + 1)):
                if self.less(j, smallest):
                    smallest = j
            if smallest == i:
                break
            self.swap(i, smallest)
            i = smallest

    def less(self, i, j):
        return self.keys[self.heap[i]] < self.keys[self.heap[j]]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.positions[self.heap[i]] = i
        self.positions[self.heap[j]] = j


# Example usage
heap = MinIndexedBinaryHeap(10)

heap.add(0, 5)
heap.add(1, 3)
heap.add(2, 8)
heap.add(3, 1)
heap.add(4, 7)

print(heap.peek())  # 3 (index of the minimum key)
print(heap.get_key(heap.peek()))  # 1 (value of the minimum key)
heap.remove(3)  # Remove the element with index 3
print(heap.peek())  # 1 (new minimum key index)
print(heap.get_key(heap.peek()))  # 3 (new minimum key value)
