class SplayTree:
    class Node:
        def __init__(self, data):
            if data is None:
                raise ValueError("Null data not allowed into tree")
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def search(self, key):
        if self.root is None:
            return None
        self.root = self.splay(self.root, key)
        return self.root if self.root.data == key else None

    def insert(self, key):
        if self.root is None:
            self.root = SplayTree.Node(key)
            return self.root
        self.root = self.splay(self.root, key)

        if key == self.root.data:
            return self.root

        new_node = SplayTree.Node(key)
        if key < self.root.data:
            new_node.right = self.root.right
            new_node.left = self.root
            self.root.right = None
        else:
            new_node.left = self.root.left
            new_node.right = self.root
            self.root.left = None

        self.root = new_node
        return self.root

    def delete(self, key):
        if self.root is None:
            return None
        self.root = self.splay(self.root, key)
        if self.root.data != key:
            return None

        if self.root.left is None:
            self.root = self.root.right
        else:
            right_subtree = self.root.right
            self.root = self.splay(self.root.left, key)
            self.root.right = right_subtree

        return self.root

    def find_max(self):
        if self.root is None:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def find_min(self):
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.data

    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def splay(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            if root.left is None:
                return root

            if key < root.left.data:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            elif key > root.left.data:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = self.left_rotate(root.left)
            return root if root.left is None else self.right_rotate(root)

        else:
            if root.right is None:
                return root

            if key > root.right.data:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)
            elif key < root.right.data:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.right_rotate(root.right)
            return root if root.right is None else self.left_rotate(root)

    def inorder(self, root, sorted_list):
        if root:
            self.inorder(root.left, sorted_list)
            sorted_list.append(root.data)
            self.inorder(root.right, sorted_list)

    def __str__(self):
        sorted_list = []
        self.inorder(self.root, sorted_list)
        return ', '.join(map(str, sorted_list)) if sorted_list else "Empty Tree"


# Example usage
splay_tree = SplayTree()
data = [2, 29, 26, -1, 10, 0, 2, 11]

for i in data:
    splay_tree.insert(i)

print("Tree after inserts:", splay_tree)

print("Insert 20:", splay_tree.insert(20))
print("Delete 29:", splay_tree.delete(29))
print("Search 10:", splay_tree.search(10))
print("Find Min:", splay_tree.find_min())
print("Find Max:", splay_tree.find_max())
print("Tree after operations:", splay_tree)
