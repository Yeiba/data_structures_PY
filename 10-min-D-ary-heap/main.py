class MinDHeap:
    def __init__(self, degree, max_nodes):
        self.d = max(2, degree)
        self.n = max(self.d, max_nodes)
        self.heap = [None] * self.n
        self.child = [0] * self.n
        self.parent = [0] * self.n
        self.sz = 0

        for i in range(self.n):
            self.parent[i] = (i - 1) // self.d
            self.child[i] = i * self.d + 1

    # Returns the number of elements currently present inside the heap
    def size(self):
        return self.sz

    # Returns true if the heap is empty
    def is_empty(self):
        return self.sz == 0

    # Clears all the elements inside the heap
    def clear(self):
        self.heap = [None] * self.n
        self.sz = 0

    # Returns the element at the top of the heap or None if the heap is empty
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    # Polls an element from the heap
    def poll(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        self.sz -= 1
        self.heap[0] = self.heap[self.sz]
        self.heap[self.sz] = None
        self.sink(0)
        return root

    # Adds a non-None element to the heap
    def add(self, elem):
        if elem is None:
            raise ValueError('No null elements please :)')
        self.heap[self.sz] = elem
        self.swim(self.sz)
        self.sz += 1

    # Moves the element at index i down to its correct position
    def sink(self, i):
        j = self.min_child(i)
        while j != -1:
            self.swap(i, j)
            i = j
            j = self.min_child(i)

    # Moves the element at index i up to its correct position
    def swim(self, i):
        while i > 0 and self.less(i, self.parent[i]):
            self.swap(i, self.parent[i])
            i = self.parent[i]

    # Finds the minimum child of the node at index i
    def min_child(self, i):
        from_idx = self.child[i]
        to_idx = min(self.sz, from_idx + self.d)
        min_index = -1

        for j in range(from_idx, to_idx):
            if j < self.sz and (min_index == -1 or self.less(j, min_index)):
                min_index = j

        return min_index

    # Checks if the element at index i is less than the element at index j
    def less(self, i, j):
        return self.heap[i].compare_to(self.heap[j]) < 0

    # Swaps the elements at indices i and j
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Example usage
class Node:
    def __init__(self, value):
        self.value = value

    def compare_to(self, other):
        return self.value - other.value

    def __repr__(self):
        return f"Node(value={self.value})"


heap = MinDHeap(3, 10)  # A ternary heap with capacity of 10

heap.add(Node(5))
heap.add(Node(3))
heap.add(Node(8))
heap.add(Node(1))
heap.add(Node(7))

print(heap.peek())  # Node(value=1)
print(heap.poll())  # Node(value=1)
print(heap.peek())  # Node(value=3)
