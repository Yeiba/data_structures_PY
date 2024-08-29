class FenwickTreeRangeUpdatePointQuery:
    def __init__(self, size):
        """
        Initialize a Fenwick Tree for a given size.
        The size should be the number of elements in the tree.
        """
        self.size = size
        self.tree = [0] * (size + 1)

    def lsb(self, i):
        """
        Returns the value of the least significant bit (LSB).
        """
        return i & -i

    def add(self, index, value):
        """
        Add 'value' to index 'index' in the Fenwick Tree.
        """
        while index <= self.size:
            self.tree[index] += value
            index += self.lsb(index)

    def update_range(self, left, right, value):
        """
        Update the range [left, right] with the given 'value'.
        """
        self.add(left, value)
        if right + 1 <= self.size:
            self.add(right + 1, -value)

    def prefix_sum(self, index):
        """
        Compute the prefix sum from the start to the given 'index'.
        """
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= self.lsb(index)
        return sum_

    def get(self, index):
        """
        Get the value at the given 'index'.
        """
        return self.prefix_sum(index)

    def __str__(self):
        """
        Print the current state of the Fenwick Tree (excluding zero index).
        """
        return str(self.tree[1:])


# Example Usage
if __name__ == "__main__":
    # Initialize Fenwick Tree with size 5
    fenwick_tree = FenwickTreeRangeUpdatePointQuery(5)

    # Initialize with some values
    initial_values = [5, 7, 3, 9, 1]
    for i, value in enumerate(initial_values, start=1):
        fenwick_tree.add(i, value)

    # Print initial state
    print("Initial Fenwick Tree:", fenwick_tree)

    # Query point values
    print("Value at index 1:", fenwick_tree.get(1))  # Output should be 5
    print("Value at index 3:", fenwick_tree.get(3))  # Output should be 15

    # Update range (2 to 4) with +3
    fenwick_tree.update_range(2, 4, 3)
    print("Fenwick Tree after range update (2 to 4) with +3:", fenwick_tree)

    # Query point values after range update
    print("Value at index 2:", fenwick_tree.get(2))  # Output should be 10
    print("Value at index 4:", fenwick_tree.get(4))  # Output should be 12
    print("Value at index 5:", fenwick_tree.get(5))  # Output should be 1
