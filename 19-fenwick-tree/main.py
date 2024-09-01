class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """
        Update the value at index `index` by adding `delta`.
        :param index: Index in the Fenwick Tree (1-based index)
        :param delta: Value to be added
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        """
        Query the prefix sum from 1 to `index`.
        :param index: Index in the Fenwick Tree (1-based index)
        :return: Prefix sum from 1 to `index`
        """
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

    def print_tree(self):
        """
        Print the Fenwick Tree array for debugging purposes.
        """
        print("Fenwick Tree:", self.tree[1:])  # Skip index 0, which is unused


# Example usage
if __name__ == "__main__":
    fenwick_tree = FenwickTree(10)

    # Update operations
    fenwick_tree.update(1, 5)
    fenwick_tree.update(3, 2)
    fenwick_tree.update(7, 7)

    # Print the tree
    print("After updates:")
    fenwick_tree.print_tree()

    # Query operations
    print("Sum from 1 to 3:", fenwick_tree.query(3))  # Output: 7 (5 + 2)
    print("Sum from 1 to 7:", fenwick_tree.query(7))  # Output: 14 (5 + 2 + 7)
    print("Sum from 1 to 10:", fenwick_tree.query(10))  # Output: 14
