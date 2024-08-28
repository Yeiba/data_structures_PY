class BinaryHeap:
    def __init__(self, initial_capacity=1):
        self.heap = []
        self.heap_size = 0
        self.heap_capacity = initial_capacity
        self.map = {}  # Dictionary to support quick removals

    @classmethod
    def from_array(cls, elems):
        heap = cls(len(elems))
        heap.heap = elems[:]
        heap.heap_size = len(elems)
        heap.build_map()
        heap.heapify()
        return heap

    def build_map(self):
        self.map.clear()
        for i, elem in enumerate(self.heap):
            self.map_add(elem, i)

    def is_empty(self):
        return self.heap_size == 0

    def clear(self):
        self.heap = []
        self.heap_size = 0
        self.map.clear()

    def size(self):
        return self.heap_size

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def poll(self):
        return self.remove_at(0)

    def contains(self, elem):
        return elem is not None and elem in self.map

    def add(self, elem):
        if elem is None:
            raise ValueError('Element cannot be None')

        if self.heap_size < self.heap_capacity:
            self.heap.append(elem)
        else:
            self.heap.append(elem)
            self.heap_capacity += 1

        self.map_add(elem, self.heap_size)
        self.heap_size += 1
        self.swim(self.heap_size - 1)

    def swap(self, i, j):
        # Swap the elements in the heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        # Update the map to reflect the new indices
        self.map_swap(self.heap[i], self.heap[j], i, j)

    def swim(self, k):
        parent = (k - 1) // 2

        while k > 0 and self.less(k, parent):
            self.swap(k, parent)
            k = parent
            parent = (k - 1) // 2

    def sink(self, k):
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = left

            if right < self.heap_size and self.less(right, left):
                smallest = right
            if left >= self.heap_size or self.less(k, smallest):
                break

            self.swap(k, smallest)
            k = smallest

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]

    def remove_at(self, i):
        if self.is_empty():
            return None

        self.heap_size -= 1
        removed_data = self.heap[i]
        self.swap(i, self.heap_size)
        self.heap.pop()

        self.map_remove(removed_data, self.heap_size)

        if i == self.heap_size:
            return removed_data

        elem = self.heap[i]
        self.sink(i)
        if self.heap[i] == elem:
            self.swim(i)

        return removed_data

    def remove(self, elem):
        if elem is None or not self.contains(elem):
            return False

        index = self.map_get(elem)
        if index is not None:
            self.remove_at(index)
            return True
        return False

    def heapify(self):
        for i in range((self.heap_size // 2) - 1, -1, -1):
            self.sink(i)

    def is_min_heap(self, k=0):
        if k >= self.heap_size:
            return True

        left = 2 * k + 1
        right = 2 * k + 2

        if left < self.heap_size and not self.less(k, left):
            return False
        if right < self.heap_size and not self.less(k, right):
            return False

        return self.is_min_heap(left) and self.is_min_heap(right)

    def map_add(self, value, index):
        if value not in self.map:
            self.map[value] = set()
        self.map[value].add(index)

    def map_remove(self, value, index):
        if value in self.map:
            self.map[value].discard(index)
            if not self.map[value]:
                del self.map[value]

    def map_get(self, value):
        if value in self.map and self.map[value]:
            return next(iter(self.map[value]))
        return None

    def map_swap(self, val1, val2, val1_index, val2_index):
        # Remove old indices
        if val1 in self.map:
            self.map[val1].discard(val1_index)
            self.map[val1].add(val2_index)
        if val2 in self.map:
            self.map[val2].discard(val2_index)
            self.map[val2].add(val1_index)

    def __str__(self):
        return str(self.heap)


# Example usage
if __name__ == "__main__":
    heap = BinaryHeap()
    heap.add(5)
    heap.add(3)
    heap.add(8)
    heap.add(1)
    heap.add(7)

    print(heap.peek())  # Output: 1 (min element)
    print(heap.poll())  # Output: 1 (removes and returns min element)
    print(heap.peek())  # Output: 3 (new min element)

    print(heap.is_min_heap())  # Output: True

    # Convert an array to a heap
    heap_from_array = BinaryHeap.from_array([5, 3, 8, 1, 7])
    print(heap_from_array)  # Min-heap representation

    # Remove a specific element
    heap.remove(7)
    print(heap)  # Heap after removal
