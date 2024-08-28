class DynamicArray:
    def __init__(self, capacity=16):
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}")
        self.capacity = capacity
        self.arr = [None] * capacity
        self.len = 0  # Length user thinks array is

    def size(self):
        return self.len

    def is_empty(self):
        return self.size() == 0

    def get(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def set(self, index, elem):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        self.arr[index] = elem

    def clear(self):
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0

    def add(self, elem):
        # Time to resize!
        if self.len >= self.capacity:
            self.capacity = 1 if self.capacity == 0 else self.capacity * 2
            new_arr = [None] * self.capacity
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index):
        if rm_index < 0 or rm_index >= self.len:
            raise IndexError("Index out of bounds")
        data = self.arr[rm_index]
        new_arr = [None] * (self.len - 1)
        for i in range(self.len):
            if i != rm_index:
                new_arr[i - (1 if i > rm_index else 0)] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.len - 1
        self.len -= 1
        return data

    def remove(self, obj):
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def index_of(self, obj):
        for i in range(self.len):
            if obj is None:
                if self.arr[i] is None:
                    return i
            else:
                if self.arr[i] == obj:
                    return i
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.len:
            result = self.arr[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        if self.len == 0:
            return "[]"
        result = "["
        for i in range(self.len - 1):
            result += str(self.arr[i]) + ", "
        return result + str(self.arr[self.len - 1]) + "]"


# Example usage:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # Output: [1, 2, 3]
arr.remove_at(1)
print(arr)  # Output: [1, 3]
print(arr.contains(2))  # Output: False
print(arr.size())  # Output: 2
