class SplayTree:
    class Node:
        def __init__(self, key, parent=None):
            self.key = key
            self.left = None
            self.right = None
            self.parent = parent

    def __init__(self):
        self.root = None

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.parent = node.parent
        if not node.parent:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.parent = node.parent
        if not node.parent:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root

    def _splay(self, node):
        while node.parent:
            if not node.parent.parent:
                if node == node.parent.left:
                    self._rotate_right(node.parent)
                else:
                    self._rotate_left(node.parent)
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                self._rotate_right(node.parent.parent)
                self._rotate_right(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                self._rotate_left(node.parent.parent)
                self._rotate_left(node.parent)
            elif node == node.parent.right and node.parent.parent.left:
                self._rotate_left(node.parent)
                self._rotate_right(node.parent)
            else:
                self._rotate_right(node.parent)
                self._rotate_left(node.parent)

    def _find(self, key):
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                self._splay(current)
                return current
        return None

    def insert(self, key):
        if not self.root:
            self.root = self.Node(key)
            return

        found_node = self._find(key)
        if found_node:
            return  # Key already exists

        new_node = self.Node(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            if self.root.left:
                self.root.left.parent = new_node
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            if self.root.right:
                self.root.right.parent = new_node
            self.root.right = None
        self.root.parent = new_node
        self.root = new_node

    def delete(self, key):
        node = self._find(key)
        if not node:
            return  # Key not found

        self._splay(node)
        if not node.left:
            self.root = node.right
            if self.root:
                self.root.parent = None
        else:
            new_root = node.left
            while new_root.right:
                new_root = new_root.right
            self._splay(new_root)
            new_root.right = node.right
            if node.right:
                node.right.parent = new_root
            self.root = new_root

    def search(self, key):
        node = self._find(key)
        return node is not None

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        self._splay(current)
        return current.key

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        self._splay(current)
        return current.key

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def in_order(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result


# Example usage
tree = SplayTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

print("In-order traversal after inserts:", tree.in_order())

print("Searching for 30:", tree.search(30))  # True
print("Searching for 25:", tree.search(25))  # False
tree.delete(30)
print("In-order traversal after deleting 30:", tree.in_order())

print("Find Min:", tree.find_min())  # 10
print("Find Max:", tree.find_max())  # 50
