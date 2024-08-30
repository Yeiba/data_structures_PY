class MinIndexedDHeap:
    def __init__(self, degree, max_size):
        if max_size <= 0:
            raise ValueError("maxSize <= 0")

        self.D = max(2, degree)
        self.N = max(self.D + 1, max_size)
        self.sz = 0

        self.child = [0] * self.N
        self.parent = [0] * self.N
        self.pm = [-1] * self.N  # Position map
        self.im = [-1] * self.N  # Inverse map
        self.values = [None] * self.N

        for i in range(self.N):
            self.parent[i] = (i - 1) // self.D
            if self.parent[i] < 0:
                self.parent[i] = None  # Root node has no parent
            self.child[i] = i * self.D + 1

    def size(self):
        return self.sz

    def is_empty(self):
        return self.sz == 0

    def contains(self, ki):
        self.key_in_bounds_or_throw(ki)
        return self.pm[ki] != -1

    def peek_min_key_index(self):
        self.is_not_empty_or_throw()
        return self.im[0]

    def poll_min_key_index(self):
        min_ki = self.peek_min_key_index()
        self.delete(min_ki)
        return min_ki

    def peek_min_value(self):
        self.is_not_empty_or_throw()
        return self.values[self.im[0]]

    def poll_min_value(self):
        min_value = self.peek_min_value()
        self.delete(self.peek_min_key_index())
        return min_value

    def insert(self, ki, value):
        if self.contains(ki):
            raise ValueError(f"Index already exists: {ki}")
        self.value_not_null_or_throw(value)
        self.pm[ki] = self.sz
        self.im[self.sz] = ki
        self.values[ki] = value
        self.sz += 1
        self.swim(self.sz - 1)

    def value_of(self, ki):
        self.key_exists_or_throw(ki)
        return self.values[ki]

    def delete(self, ki):
        self.key_exists_or_throw(ki)
        i = self.pm[ki]
        self.swap(i, self.sz - 1)
        self.sz -= 1
        self.sink(i)
        self.swim(i)
        value = self.values[ki]
        self.values[ki] = None
        self.pm[ki] = -1
        self.im[self.sz] = -1
        return value

    def update(self, ki, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        i = self.pm[ki]
        old_value = self.values[ki]
        self.values[ki] = value
        self.sink(i)
        self.swim(i)
        return old_value

    def decrease(self, ki, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        if self.less(value, self.values[ki]):
            self.values[ki] = value
            self.swim(self.pm[ki])

    def increase(self, ki, value):
        self.key_exists_and_value_not_null_or_throw(ki, value)
        if self.less(self.values[ki], value):
            self.values[ki] = value
            self.sink(self.pm[ki])

    def swim(self, i):
        while i > 0 and self.less(i, self.parent[i]):
            self.swap(i, self.parent[i])
            i = self.parent[i]

    def sink(self, i):
        while True:
            min_child_idx = self.min_child(i)
            if min_child_idx == -1:
                break
            self.swap(i, min_child_idx)
            i = min_child_idx

    def min_child(self, i):
        min_idx = -1
        from_idx = self.child[i]
        to = min(self.sz, from_idx + self.D)
        for j in range(from_idx, to):
            if j < self.sz and (min_idx == -1 or self.less(j, min_idx)):
                min_idx = j
        return min_idx

    def swap(self, i, j):
        self.im[i], self.im[j] = self.im[j], self.im[i]
        self.pm[self.im[i]] = i
        self.pm[self.im[j]] = j

    def less(self, i, j):
        return self.values[self.im[i]] < self.values[self.im[j]]

    def value_not_null_or_throw(self, value):
        if value is None:
            raise ValueError("value cannot be null")

    def key_in_bounds_or_throw(self, ki):
        if ki < 0 or ki >= self.N:
            raise IndexError(f"Key index out of bounds: {ki}")

    def key_exists_or_throw(self, ki):
        if not self.contains(ki):
            raise ValueError(f"Index does not exist: {ki}")

    def key_exists_and_value_not_null_or_throw(self, ki, value):
        self.key_exists_or_throw(ki)
        self.value_not_null_or_throw(value)

    def is_not_empty_or_throw(self):
        if self.is_empty():
            raise ValueError("Priority queue underflow")

    def is_min_heap(self):
        return self.is_min_heap_rec(0)

    def is_min_heap_rec(self, i):
        from_idx = self.child[i]
        to = min(self.sz, from_idx + self.D)
        for j in range(from_idx, to):
            if j < self.sz and not self.less(i, j):
                return False
            if j < self.sz and not self.is_min_heap_rec(j):
                return False
        return True

    def __str__(self):
        return str(self.im[:self.sz])


# Example usage
if __name__ == "__main__":
    heap = MinIndexedDHeap(3, 10)  # Ternary heap

    heap.insert(0, 5)
    heap.insert(1, 3)
    heap.insert(2, 8)
    heap.insert(3, 1)
    heap.insert(4, 7)

    print(heap.peek_min_key_index())  # 3 (index of the minimum key)
    print(heap.peek_min_value())  # 1 (value of the minimum key)

    heap.delete(3)  # Remove the element with index 3

    print(heap.peek_min_key_index())  # 1 (new minimum key index)
    print(heap.peek_min_value())  # 3 (new minimum key value)
