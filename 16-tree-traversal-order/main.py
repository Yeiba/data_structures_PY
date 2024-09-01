class BinaryTree:
    def __init__(self):
        self.root = None

    class TreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def insert(self, key):
        if self.root is None:
            self.root = self.TreeNode(key)
        else:
            self._insert_node(self.root, key)

    def _insert_node(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = self.TreeNode(key)
            else:
                self._insert_node(node.left, key)
        else:
            if node.right is None:
                node.right = self.TreeNode(key)
            else:
                self._insert_node(node.right, key)

    # In-order traversal (Left, Root, Right)
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.key)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order traversal (Root, Left, Right)
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.key)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order traversal (Left, Right, Root)
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.key)
        return result

    # Level-order traversal (Breadth-First Search)
    def level_order_traversal(self):
        result = []
        queue = []

        if self.root:
            queue.append(self.root)

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.key)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result


# Example usage
tree = BinaryTree()
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(8)
tree.insert(12)
tree.insert(17)
tree.insert(25)

# [8, 10, 12, 15, 17, 20, 25]
print("In-order Traversal:", tree.in_order_traversal(tree.root))
# [15, 10, 8, 12, 20, 17, 25]
print("Pre-order Traversal:", tree.pre_order_traversal(tree.root))
# [8, 12, 10, 17, 25, 20, 15]
print("Post-order Traversal:", tree.post_order_traversal(tree.root))
# [15, 10, 20, 8, 12, 17, 25]
print("Level-order Traversal:", tree.level_order_traversal())
