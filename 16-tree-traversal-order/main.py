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

    def search(self, node):
        if self.root is None:
            return None
        self.root = self.splay(node)
        return self.root.data if self.root.data == node else None

    def insert(self, node):
        if self.root is None:
            self.root = SplayTree.Node(node)
            return self.root
        self.splay(node)
        left, right = self.split(node)
        self.root = SplayTree.Node(node)
        self.root.left = left
        self.root.right = right
        return self.root

    def delete(self, node):
        if self.root is None:
            return None
        search_result = self.splay(node)
        if search_result.data != node:
            return None
        left_subtree = self.root.left
        right_subtree = self.root.right
        self.root.left = None
        self.root.right = None
        self.root = self.join(left_subtree, right_subtree)
        return self.root

    def find_max(self):
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.data

    def find_min(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.data

    def right_rotate(self, node):
        p = node.left
        node.left = p.right
        p.right = node
        return p

    def left_rotate(self, node):
        p = node.right
        node.right = p.left
        p.left = node
        return p

    def splay_util(self, root, key):
        if root is None or root.data == key:
            return root
        if root.data > key:
            if root.left is None:
                return root
            if root.left.data > key:
                root.left.left = self.splay_util(root.left.left, key)
                root = self.right_rotate(root)
            elif root.left.data < key:
                root.left.right = self.splay_util(root.left.right, key)
                if root.left.right is not None:
                    root.left = self.left_rotate(root.left)
            return root.left is None and root or self.right_rotate(root)
        else:
            if root.right is None:
                return root
            if root.right.data > key:
                root.right.left = self.splay_util(root.right.left, key)
                if root.right.left is not None:
                    root.right = self.right_rotate(root.right)
            elif root.right.data < key:
                root.right.right = self.splay_util(root.right.right, key)
                root = self.left_rotate(root)
            return root.right is None and root or self.left_rotate(root)

    def splay(self, node):
        if self.root is None:
            return None
        self.root = self.splay_util(self.root, node)
        return self.root

    def split(self, node):
        if node > self.root.data:
            right = self.root.right
            left = self.root
            left.right = None
        else:
            left = self.root.left
            right = self.root
            right.left = None
        return left, right

    def join(self, L, R):
        if L is None:
            self.root = R
            return R
        self.root = self.splay_util(L, self.find_max(L))
        self.root.right = R
        return self.root

    def inorder(self, root, sorted_list=None):
        if sorted_list is None:
            sorted_list = []
        if root is None:
            return sorted_list
        self.inorder(root.left, sorted_list)
        sorted_list.append(root.data)
        self.inorder(root.right, sorted_list)
        return sorted_list

    def preorder(self, root, sorted_list=None):
        if sorted_list is None:
            sorted_list = []
        if root is None:
            return sorted_list
        sorted_list.append(root.data)
        self.preorder(root.left, sorted_list)
        self.preorder(root.right, sorted_list)
        return sorted_list

    def postorder(self, root, sorted_list=None):
        if sorted_list is None:
            sorted_list = []
        if root is None:
            return sorted_list
        self.postorder(root.left, sorted_list)
        self.postorder(root.right, sorted_list)
        sorted_list.append(root.data)
        return sorted_list

    def level_order(self, root):
        result = []
        if root is None:
            return result
        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result

    def traverse(self, order="IN_ORDER"):
        if order == "PRE_ORDER":
            return self.preorder(self.root)
        elif order == "IN_ORDER":
            return self.inorder(self.root)
        elif order == "POST_ORDER":
            return self.postorder(self.root)
        elif order == "LEVEL_ORDER":
            return self.level_order(self.root)
        else:
            raise ValueError("Unknown traversal order")

    def __str__(self):
        return ', '.join(map(str, self.inorder(self.root))) if self.root else "Empty Tree"


# Example usage
if __name__ == "__main__":
    splay_tree = SplayTree()
    data = [2, 29, 26, -1, 10, 0, 2, 11]

    for i in data:
        splay_tree.insert(i)

    print("Tree:", splay_tree)

    print("Pre-order traversal:", splay_tree.traverse("PRE_ORDER"))
    print("In-order traversal:", splay_tree.traverse("IN_ORDER"))
    print("Post-order traversal:", splay_tree.traverse("POST_ORDER"))
    print("Level-order traversal:", splay_tree.traverse("LEVEL_ORDER"))
