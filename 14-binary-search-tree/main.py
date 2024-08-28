class BinarySearchTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.node_count = 0
        self.root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.node_count

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self._add(self.root, elem)
            self.node_count += 1
            return True

    def _add(self, node, elem):
        if node is None:
            return BinarySearchTree.Node(elem)

        if elem < node.data:
            node.left = self._add(node.left, elem)
        else:
            node.right = self._add(node.right, elem)

        return node

    def remove(self, elem):
        if self.contains(elem):
            self.root = self._remove(self.root, elem)
            self.node_count -= 1
            return True
        return False

    def _remove(self, node, elem):
        if node is None:
            return None

        if elem < node.data:
            node.left = self._remove(node.left, elem)
        elif elem > node.data:
            node.right = self._remove(node.right, elem)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._remove(node.right, min_node.data)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def contains(self, elem):
        return self._contains(self.root, elem)

    def _contains(self, node, elem):
        if node is None:
            return False

        if elem < node.data:
            return self._contains(node.left, elem)
        elif elem > node.data:
            return self._contains(node.right, elem)
        else:
            return True

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def traverse(self, order):
        if order == 'PRE_ORDER':
            return self._pre_order_traversal()
        elif order == 'IN_ORDER':
            return self._in_order_traversal()
        elif order == 'POST_ORDER':
            return self._post_order_traversal()
        elif order == 'LEVEL_ORDER':
            return self._level_order_traversal()
        else:
            return []

    def _pre_order_traversal(self):
        stack = [self.root]
        result = []

        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                stack.append(node.right)
                stack.append(node.left)

        return iter(result)

    def _in_order_traversal(self):
        stack = []
        result = []
        current = self.root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.data)
                current = current.right

        return iter(result)

    def _post_order_traversal(self):
        stack1 = [self.root]
        stack2 = []
        result = []

        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)
                stack1.append(node.left)
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().data)

        return iter(result)

    def _level_order_traversal(self):
        queue = [self.root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)

        return iter(result)


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.add(10)
    bst.add(5)
    bst.add(15)
    print(list(bst.traverse('IN_ORDER')))  # [5, 10, 15]
    print(bst.contains(10))  # True
    print(bst.height())  # 2
    bst.remove(10)
    print(bst.contains(10))  # False
    print(list(bst.traverse('IN_ORDER')))  # [5, 15]
