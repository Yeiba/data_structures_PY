class IndexedMinHeap:
    def __init__(self):
        self.heap = []
        self.index_map = {}

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
            if self.heap[index][1] < self.heap[parent_index][1]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def extract_min(self):
        try:
            if not self.heap:
                raise IndexError("Heap is empty")

            min_node = self.heap[0]
            last_node = self.heap.pop()
            if self.heap:
                self.heap[0] = last_node
                self.index_map[last_node[0]] = 0
                self._heapify_down(0)
            del self.index_map[min_node[0]]
            return min_node
        except IndexError as e:
            print("Error:", e)

    def _heapify_down(self, index):
        smallest = index
        left_child = self._get_left_child(index)
        right_child = self._get_right_child(index)

        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[smallest][1]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[smallest][1]:
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def update(self, index, new_value):
        try:
            if index not in self.index_map:
                raise ValueError("Index does not exist in the heap")

            heap_index = self.index_map[index]
            old_value = self.heap[heap_index][1]
            self.heap[heap_index] = (index, new_value)

            if new_value < old_value:
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

    heap = IndexedMinHeap()

    # Insert elements
    heap.insert(1, 10)
    heap.insert(2, 5)
    heap.insert(3, 15)
    heap.insert(4, 8)

    print("Heap:", heap)  # Print the heap

    # Extract the minimum
    print("Extract Min:", heap.extract_min())
    print("Heap after extraction:", heap)

    # Update value
    heap.update(3, 4)
    print("Heap after update:", heap)

    # Get value
    print("Value at index 2:", heap.get(2))

    # Check if empty
    print("Heap Size:", heap.size())
    print("Is Heap Empty?", heap.is_empty())

    # Test error handling

    heap.update(99, 20)  # Should raise an error

    heap.get(99)  # Should raise an error
