class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def extract_min(self):
        try:
            if len(self.heap) == 0:
                raise IndexError("Heap is empty")

            if len(self.heap) == 1:
                return self.heap.pop()

            min_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return min_value
        except IndexError as e:
            print("Error:", e)

    def heapify_down(self, index):
        smallest = index

        if self.has_left_child(index) and self.left_child(index) < self.heap[smallest]:
            smallest = self.get_left_child_index(index)

        if self.has_right_child(index) and self.right_child(index) < self.heap[smallest]:
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def peek(self):
        try:
            if len(self.heap) == 0:
                raise IndexError("Heap is empty")
            return self.heap[0]
        except IndexError as e:
            print("Error:", e)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


# Example usage:
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(14)
min_heap.insert(9)
min_heap.insert(2)

print(min_heap.peek())  # Output: 2

print(min_heap.extract_min())  # Output: 2
print(min_heap.extract_min())  # Output: 5
print(min_heap.extract_min())  # Output: 9

print(min_heap.size())  # Output: 2

print(min_heap.is_empty())  # Output: False

print(min_heap.extract_min())  # Output: 10
print(min_heap.extract_min())  # Output: 14

print(min_heap.is_empty())  # Output: True
