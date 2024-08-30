class DAryMinHeap:
    def __init__(self, d):
        self.d = d  # Number of children per node
        self.heap = []  # Array to store heap elements

    def get_parent_index(self, index):
        return (index - 1) // self.d

    def get_child_index(self, parent_index, child_index):
        return self.d * parent_index + child_index + 1

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent_index(index)
            if self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def extract_min(self):
        try:
            if not self.heap:
                raise IndexError("Heap is empty")

            min_value = self.heap[0]
            last_value = self.heap.pop()
            if self.heap:
                self.heap[0] = last_value
                self.heapify_down(0)
            return min_value
        except IndexError as e:
            print("Error:", e)

    def heapify_down(self, index):
        size = len(self.heap)
        smallest = index
        for i in range(self.d):
            child_index = self.get_child_index(index, i)
            if child_index < size and self.heap[child_index] < self.heap[smallest]:
                smallest = child_index
        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def peek(self):
        try:
            if not self.heap:
                raise IndexError("Heap is empty")
            return self.heap[0]
        except IndexError as e:
            print("Error:", e)

    def get_size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)


# Example usage
if __name__ == "__main__":
    d_ary_heap = DAryMinHeap(3)  # A ternary heap (D=3)

    d_ary_heap.insert(10)
    d_ary_heap.insert(5)
    d_ary_heap.insert(20)
    d_ary_heap.insert(1)
    d_ary_heap.insert(15)

    print("Heap:", d_ary_heap)  # Print heap structure
    print("Min:", d_ary_heap.peek())  # Output: Min: 1

    print("Extract Min:", d_ary_heap.extract_min())  # Output: Extract Min: 1
    # Print heap structure after extraction
    print("Heap after extraction:", d_ary_heap)

    print("Heap size:", d_ary_heap.get_size())  # Print the size of the heap
    # Check if the heap is empty
    print("Is heap empty?", d_ary_heap.is_empty())
