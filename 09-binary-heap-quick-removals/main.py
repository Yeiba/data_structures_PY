class BinaryHeapQuickRemovals:
    def __init__(self, initial_capacity=1):
        self.heap = [None] * initial_capacity
        self.heap_size = 0
        self.heap_capacity = initial_capacity
        self.map = {}

    @classmethod
    def from_array(cls, elems):
        heap = cls(len(elems))
        heap.heap = elems[:]
        heap.heap_size = len(elems)
        heap.heapify()
        return heap

    @classmethod
    def from_collection(cls, collection):
        heap = cls(len(collection))
        for elem in collection:
            heap.add(elem)
        return heap

    def is_empty(self):
        return self.heap_size == 0

    def clear(self):
        self.heap = [None] * self.heap_capacity
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
            raise ValueError("Element cannot be null")

        if self.heap_size >= self.heap_capacity:
            self.heap_capacity *= 2
            new_heap = [None] * self.heap_capacity
            new_heap[:self.heap_size] = self.heap
            self.heap = new_heap

        self.heap[self.heap_size] = elem
        self.map_add(elem, self.heap_size)
        self.heap_size += 1
        self.swim(self.heap_size - 1)

    def swim(self, k):
        while k > 0:
            parent = (k - 1) // 2
            if self.less(k, parent):
                self.swap(parent, k)
                k = parent
            else:
                break

    def sink(self, k):
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = k

            if left < self.heap_size and self.less(left, smallest):
                smallest = left
            if right < self.heap_size and self.less(right, smallest):
                smallest = right

            if smallest == k:
                break

            self.swap(k, smallest)
            k = smallest

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]

    def swap(self, i, j):
        if i == j:
            return

        # Swap elements in heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        # Update map with new positions
        self.map_swap(self.heap[i], self.heap[j], i, j)

    def remove(self, elem):
        if elem is None:
            return False

        index = self.map_get(elem)
        if index is not None:
            self.remove_at(index)
            return True
        return False

    def remove_at(self, i):
        if self.is_empty():
            return None

        removed_data = self.heap[i]
        last_elem = self.heap[self.heap_size - 1]
        self.heap[i] = last_elem
        self.heap_size -= 1
        self.heap.pop()

        self.map_remove(removed_data, i)

        if i < self.heap_size:
            self.map_add(last_elem, i)
            self.sink(i)
            if self.heap[i] == last_elem:
                self.swim(i)

        return removed_data

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
            return max(self.map[value])
        return None

    def map_swap(self, val1, val2, val1_index, val2_index):
        if val1 in self.map:
            self.map[val1].discard(val1_index)
            self.map[val1].add(val2_index)
        if val2 in self.map:
            self.map[val2].discard(val2_index)
            self.map[val2].add(val1_index)

    def __str__(self):
        return str(self.heap[:self.heap_size])


# Example usage
heap = BinaryHeapQuickRemovals()
heap.add(5)
heap.add(3)
heap.add(8)
heap.add(1)
heap.add(7)

print(heap.peek())  # 1 (min element)
print(heap.poll())  # 1 (removes and returns min element)
print(heap.peek())  # 3 (new min element)

print(heap.is_min_heap())  # True

# Convert an array to a heap
heap_from_array = BinaryHeapQuickRemovals.from_array([5, 3, 8, 1, 7])
print(heap_from_array)  # Min-heap representation

# Remove a specific element
heap.remove(7)
print(heap)  # Heap after removal
