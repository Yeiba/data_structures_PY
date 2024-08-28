class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.bf = 0  # Balance factor
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def height(self):
        return self.root.height if self.root else 0

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.size() == 0

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        while node is not None:
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
            return False
        inserted, self.root = self._insert(self.root, value)
        if inserted:
            self.node_count += 1
        return inserted

    def _insert(self, node, value):
        if node is None:
            return True, Node(value)

        cmp = self._compare(value, node.value)

        if cmp < 0:
            inserted, node.left = self._insert(node.left, value)
        elif cmp > 0:
            inserted, node.right = self._insert(node.right, value)
        else:
            return False, node  # Duplicate value

        if inserted:
            self._update(node)
            node = self._balance(node)
        return inserted, node

    def _update(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        node.height = 1 + max(left_height, right_height)
        node.bf = right_height - left_height

    def _balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self._right_rotation(node)
            else:
                return self._left_right_case(node)

        if node.bf == 2:
            if node.right.bf >= 0:
                return self._left_rotation(node)
            else:
                return self._right_left_case(node)

        return node

    def _left_right_case(self, node):
        node.left = self._left_rotation(node.left)
        return self._right_rotation(node)

    def _right_left_case(self, node):
        node.right = self._right_rotation(node.right)
        return self._left_rotation(node)

    def _left_rotation(self, node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        self._update(node)
        self._update(new_parent)
        return new_parent

    def _right_rotation(self, node):
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        self._update(new_parent)
        self._update(node)
        return new_parent

    def remove(self, value):
        removed, self.root = self._remove(self.root, value)
        if removed:
            self.node_count -= 1
        return removed

    def _remove(self, node, value):
        if node is None:
            return False, node

        cmp = self._compare(value, node.value)

        if cmp < 0:
            removed, node.left = self._remove(node.left, value)
        elif cmp > 0:
            removed, node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return True, node.right
            elif node.right is None:
                return True, node.left
            else:
                if node.left.height > node.right.height:
                    successor_value = self._find_max(node.left)
                    node.value = successor_value
                    removed, node.left = self._remove(
                        node.left, successor_value)
                else:
                    successor_value = self._find_min(node.right)
                    node.value = successor_value
                    removed, node.right = self._remove(
                        node.right, successor_value)

        if removed:
            self._update(node)
            node = self._balance(node)
        return removed, node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node.value

    def _compare(self, value1, value2):
        if isinstance(value1, str) and isinstance(value2, str):
            return (value1 > value2) - (value1 < value2)
        else:
            return (value1 > value2) - (value1 < value2)

    def __iter__(self):
        stack = []
        trav = self.root

        while stack or trav:
            while trav:
                stack.append(trav)
                trav = trav.left

            node = stack.pop()
            yield node.value
            trav = node.right

    def validate_bst_invariant(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self.validate_bst_invariant(node.left, min_val, node.value) and
                self.validate_bst_invariant(node.right, node.value, max_val))


# Example Usage
if __name__ == "__main__":
    avl_tree = AVLTree()

    # Insert values
    values = [10, 20, 30, 15, 25, 5]
    for value in values:
        avl_tree.insert(value)

    # Print values in sorted order
    print("In-order traversal:", list(avl_tree))

    # Remove a value
    avl_tree.remove(20)
    print("In-order traversal after removing 20:", list(avl_tree))

    # Validate BST invariant
    print("Is the tree a valid BST?", avl_tree.validate_bst_invariant())
