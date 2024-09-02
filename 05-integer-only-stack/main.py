

class IntegerStack:
    def __init__(self, first_elem=None):
        if first_elem is not None and not isinstance(first_elem, int):
            raise TypeError("Only integers are allowed")
        self.head = self.Node(
            first_elem) if first_elem is not None else first_elem
        self._size = 1 if first_elem is not None else 0

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, elem):
        if not isinstance(elem, int):
            raise TypeError("Only integers are allowed")
        new_node = self.Node(elem)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        popped_node = self.head
        self.head = self.head.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.head.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


# Example usage:
stack = IntegerStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.size())  # 2

for item in stack:
    print(item)  # 2, 1

# The following will throw an error
# stack.push("hello")  # TypeError: Only integers are allowed
