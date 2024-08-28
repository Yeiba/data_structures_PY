class IntArray:
    DEFAULT_CAP = 8

    def __init__(self, capacity=DEFAULT_CAP):
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}")
        self.capacity = capacity
        self.arr = [0] * capacity
        self.len = 0

    # Initialize with an existing array
    @classmethod
    def from_array(cls, array):
        if array is None:
            raise ValueError("Array cannot be null")
        int_array = cls(len(array))
        int_array.arr = array[:]
        int_array.len = int_array.capacity = len(array)
        return int_array

    def size(self):
        return self.len

    def is_empty(self):
        return self.len == 0

    def get(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def set(self, index, elem):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        self.arr[index] = elem

    def add(self, elem):
        if self.len >= self.capacity:
            self.capacity = 1 if self.capacity == 0 else self.capacity * 2
            new_arr = [0] * self.capacity
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index):
        if rm_index < 0 or rm_index >= self.len:
            raise IndexError("Index out of bounds")
        for i in range(rm_index, self.len - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.len - 1] = 0
        self.len -= 1

    def remove(self, elem):
        for i in range(self.len):
            if self.arr[i] == elem:
                self.remove_at(i)
                return True
        return False

    def reverse(self):
        for i in range(self.len // 2):
            tmp = self.arr[i]
            self.arr[i] = self.arr[self.len - i - 1]
            self.arr[self.len - i - 1] = tmp

    def binary_search(self, key):
        low, high = 0, self.len - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = self.arr[mid]
            if mid_val < key:
                low = mid + 1
            elif mid_val > key:
                high = mid - 1
            else:
                return mid
        return -1  # Not found

    def sort(self):
        self.arr[:self.len] = sorted(self.arr[:self.len])

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
        return "[" + ", ".join(map(str, self.arr[:self.len])) + "]"


# Example usage
if __name__ == "__main__":
    ar = IntArray(50)
    ar.add(3)
    ar.add(7)
    ar.add(6)
    ar.add(-2)

    ar.sort()  # [-2, 3, 6, 7]

    for i in range(ar.size()):
        print(ar.get(i))  # Prints -2, 3, 6, 7

    print(ar)  # Prints [-2, 3, 6, 7]
