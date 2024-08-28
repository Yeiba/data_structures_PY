class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.color = True  # RED by default
        self.left = None
        self.right = None


class RedBlackTree:
    RED = True
    BLACK = False

    def __init__(self):
        self.root = None
        self.node_count = 0

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.size() == 0

    def contains(self, value):
        node = self.root
        while node:
            cmp = self._compare(value, node.value)
            if cmp < 0:
                node = node.left
            elif cmp > 0:
                node = node.right
            else:
                return True
        return False

    def insert(self, value):
        if value is None:
            raise ValueError("Value cannot be None")

        if self.root is None:
            self.root = Node(value)
            self.root.color = self.BLACK
            self.node_count += 1
            return True

        node = self.root
        while True:
            cmp = self._compare(value, node.value)

            if cmp < 0:
                if node.left is None:
                    node.left = Node(value, node)
                    self._insertion_relabel(node.left)
                    self.node_count += 1
                    return True
                node = node.left
            elif cmp > 0:
                if node.right is None:
                    node.right = Node(value, node)
                    self._insertion_relabel(node.right)
                    self.node_count += 1
                    return True
                node = node.right
            else:
                return False

    def _insertion_relabel(self, node):
        while node != self.root and node.parent.color == self.RED:
            parent = node.parent
            grand_parent = parent.parent

            if parent == grand_parent.left:
                uncle = grand_parent.right
                if uncle and uncle.color == self.RED:
                    parent.color = self.BLACK
                    grand_parent.color = self.RED
                    uncle.color = self.BLACK
                    node = grand_parent
                else:
                    if node == parent.right:
                        node = parent
                        self._left_rotate(node)
                    parent.color = self.BLACK
                    grand_parent.color = self.RED
                    self._right_rotate(grand_parent)
            else:
                uncle = grand_parent.left
                if uncle and uncle.color == self.RED:
                    parent.color = self.BLACK
                    grand_parent.color = self.RED
                    uncle.color = self.BLACK
                    node = grand_parent
                else:
                    if node == parent.left:
                        node = parent
                        self._right_rotate(node)
                    parent.color = self.BLACK
                    grand_parent.color = self.RED
                    self._left_rotate(grand_parent)

        self.root.color = self.BLACK

    def _swap_colors(self, a, b):
        a.color, b.color = b.color, a.color

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def _compare(self, value1, value2):
        if value1 < value2:
            return -1
        if value1 > value2:
            return 1
        return 0


# Example Usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()

    # Insert values
    values = [10, 20, 30, 15, 25, 5]
    for value in values:
        rb_tree.insert(value)

    # Check the contents
    print("Tree contains 15:", rb_tree.contains(15))
    print("Tree contains 40:", rb_tree.contains(40))

    # Print size of the tree
    print("Size of the tree:", rb_tree.size())
