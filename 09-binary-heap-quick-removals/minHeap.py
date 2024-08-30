class MinHeapQR:
    def __init__(self):
        self.heap = []
        self.index_map = {}  # Map to store the positions of elements for quick removals

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
        # Update the map with the new positions
        self.index_map[self.heap[index1]] = index1
        self.index_map[self.heap[index2]] = index2

    def insert(self, value):
        self.heap.append(value)
        self.index_map[value] = len(self.heap) - 1
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

            min_value = self.heap[0]
            end_value = self.heap.pop()
            self.index_map.pop(min_value, None)

            if len(self.heap) > 0:
                self.heap[0] = end_value
                self.index_map[end_value] = 0
                self.heapify_down()

            return min_value
        except IndexError as e:
            print("Error:", e)

    def heapify_down(self):
        index = 0
        smallest = index

        if self.has_left_child(index) and self.left_child(index) < self.heap[smallest]:
            smallest = self.get_left_child_index(index)

        if self.has_right_child(index) and self.right_child(index) < self.heap[smallest]:
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down()

    def remove(self, value):
        if value not in self.index_map:
            return False

        index = self.index_map[value]
        end_value = self.heap.pop()
        self.index_map.pop(value)

        if index < len(self.heap):
            self.heap[index] = end_value
            self.index_map[end_value] = index
            self.heapify_up_from_index(index)
            self.heapify_down()

        return True

    def heapify_up_from_index(self, index):
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

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


# Example usage
if __name__ == "__main__":
    min_heap = MinHeapQR()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(14)
    min_heap.insert(9)
    min_heap.insert(2)

    print("Min:", min_heap.peek())  # Output: Min: 2

    print("Extract Min:", min_heap.extract_min())  # Output: Extract Min: 2
    print("Extract Min:", min_heap.extract_min())  # Output: Extract Min: 5

    min_heap.insert(3)
    print("Min:", min_heap.peek())  # Output: Min: 3

    min_heap.remove(3)
    print("Heap:", min_heap.heap)  # Output: Heap: [9, 10, 14]

    print("Index of 14:", min_heap.index_map.get(
        14, "Not found"))  # Output: Index of 14: 2
