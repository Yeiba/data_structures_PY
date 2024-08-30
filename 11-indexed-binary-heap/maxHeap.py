class IndexedMaxHeap:
    def __init__(self):
        self.heap = []       # List to store heap elements
        self.index_map = {}  # Dictionary to map index to its position in the heap

    def _get_parent(self, index):
        return (index - 1) // 2

    def _get_left_child(self, index):
        return 2 * index + 1

    def _get_right_child(self, index):
        return 2 * index + 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        self.index_map[self.heap[index1][0]] = index1
        self.index_map[self.heap[index2][0]] = index2

    def insert(self, index, value):
        try:
            if index in self.index_map:
                raise ValueError("Index already exists in the heap")

            node = (index, value)
            self.heap.append(node)
            self.index_map[index] = len(self.heap) - 1
            self._heapify_up(len(self.heap) - 1)
        except ValueError as e:
            print("Error:", e)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self._get_parent(index)
            if self.heap[index][1] > self.heap[parent_index][1]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def extract_max(self):
        try:
            if not self.heap:
                raise IndexError("Heap is empty")

            max_node = self.heap[0]
            last_node = self.heap.pop()
            if self.heap:
                self.heap[0] = last_node
                self.index_map[last_node[0]] = 0
                self._heapify_down(0)
            del self.index_map[max_node[0]]
            return max_node
        except IndexError as e:
            print("Error:", e)

    def _heapify_down(self, index):
        largest = index
        left_child = self._get_left_child(index)
        right_child = self._get_right_child(index)

        if left_child < len(self.heap) and self.heap[left_child][1] > self.heap[largest][1]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child][1] > self.heap[largest][1]:
            largest = right_child

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def update(self, index, new_value):
        try:
            if index not in self.index_map:
                raise ValueError("Index does not exist in the heap")

            heap_index = self.index_map[index]
            old_value = self.heap[heap_index][1]
            self.heap[heap_index] = (index, new_value)

            if new_value > old_value:
                self._heapify_up(heap_index)
            else:
                self._heapify_down(heap_index)
        except ValueError as e:
            print("Error:", e)

    def get(self, index):
        try:
            if index not in self.index_map:
                raise ValueError("Index does not exist in the heap")
            heap_index = self.index_map[index]
            return self.heap[heap_index][1]
        except ValueError as e:
            print("Error:", e)

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


# Example usage:
if __name__ == "__main__":

    heap = IndexedMaxHeap()

    # Insert elements
    heap.insert(1, 10)
    heap.insert(2, 20)
    heap.insert(3, 15)
    heap.insert(4, 30)

    print("Heap:", heap)  # Print the heap

    # Extract the maximum
    print("Extract Max:", heap.extract_max())
    print("Heap after extraction:", heap)

    # Update value
    heap.update(3, 25)
    print("Heap after update:", heap)

    # Get value
    print("Value at index 2:", heap.get(2))

    # Check if empty
    print("Heap Size:", heap.size())
    print("Is Heap Empty?", heap.is_empty())

    # Test error handling

    heap.update(99, 40)  # Should raise an error

    heap.get(99)  # Should raise an error
