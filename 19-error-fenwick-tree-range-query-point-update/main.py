class FenwickTreeRangeQueryPointUpdate:
    def __init__(self, sz_or_values):
        if isinstance(sz_or_values, list):
            values = sz_or_values
            if values is None:
                raise ValueError("Values array cannot be null!")

            self.N = len(values) + 1
            self.tree = [0] * self.N
            for i in range(len(values)):
                self.add(i + 1, values[i])
        else:
            sz = sz_or_values
            self.N = sz + 1
            self.tree = [0] * self.N

    def lsb(self, i):
        return i & -i

    def prefix_sum(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.tree[i]
            i -= self.lsb(i)
        return sum_

    def range_sum(self, left, right):
        if right < left:
            raise ValueError("Make sure right >= left")
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def get(self, i):
        return self.range_sum(i, i)

    def add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self.lsb(i)

    def set(self, i, v):
        current_value = self.get(i)
        self.add(i, v - current_value)

    def __str__(self):
        # Show the tree without the initial zero element
        return str(self.tree[1:])  # Exclude the first element (zero index)


# Example usage
if __name__ == "__main__":
    # Initialize with a size of 10
    fenwick_tree = FenwickTreeRangeQueryPointUpdate(
        [0] * 10)  # Start with zero values

    # Add values to specific indices
    fenwick_tree.add(1, 5)
    fenwick_tree.add(2, 3)
    fenwick_tree.add(3, 7)
    fenwick_tree.add(4, 6)

    # Sum of range [1, 3]
    # Expected Output: 15
    print("Sum of range [1, 3]:", fenwick_tree.range_sum(1, 3))

    # Get the value at index 3
    print("Value at index 3:", fenwick_tree.get(3))  # Expected Output: 7

    # Set the value at index 3 to 10
    fenwick_tree.set(3, 10)

    # Print the tree
    # Expected Output: [5, 8, 10, 24, 0, 0, 0, 0, 0, 0]
    print("Fenwick Tree:", fenwick_tree)
