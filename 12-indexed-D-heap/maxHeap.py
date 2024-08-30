class IndexedMaxDHeap:
    def __init__(self, d=2):
        self.d = d
        self.heap = []
        self.index_map = {}

    def _get_parent(self, index):
        return (index - 1) // self.d

    def _get_child(self, index, child_number):
        return self.d * index + child_number + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i][1]] = i
        self.index_map[self.heap[j][1]] = j

    def _heapify_down(self, index):
        largest = index
        for i in range(self.d):
            child_index = self._get_child(index, i)
            if child_index < len(self.heap) and self.heap[child_index][0] > self.heap[largest][0]:
                largest = child_index

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _heapify_up(self, index):
        parent_index = self._get_parent(index)
        if index > 0 and self.heap[index][0] > self.heap[parent_index][0]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def insert(self, index, value):
        if index in self.index_map:
            raise ValueError("Index already exists in the heap")

        new_node = (value, index)
        self.heap.append(new_node)
        self.index_map[index] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def remove(self, index):
        if index not in self.index_map:
            raise ValueError("Index does not exist in the heap")

        heap_index = self.index_map.pop(index)
        self._swap(heap_index, len(self.heap) - 1)
        self.heap.pop()

        if heap_index < len(self.heap):
            self._heapify_up(heap_index)
            self._heapify_down(heap_index)

    def get(self, index):
        if index not in self.index_map:
            raise ValueError("Index does not exist in the heap")
        return self.heap[self.index_map[index]][0]

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0][0]

    def print_heap(self):
        print([value for value, _ in self.heap])


# Example usage
heap = IndexedMaxDHeap(d=3)  # Ternary heap

heap.insert(1, 10)
heap.insert(2, 20)
heap.insert(3, 30)
heap.insert(4, 40)
heap.insert(5, 50)

print("Heap:")
heap.print_heap()

print("Value at index 2:", heap.get(2))  # Should be 20

heap.remove(2)

print("Heap after removing index 2:")
heap.print_heap()

print("Value at index 3:", heap.get(3))  # Should be 30 after adjustments
