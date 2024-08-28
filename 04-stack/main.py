class Stack:
    def __init__(self, first_elem=None):
        self.list = []
        if first_elem is not None:
            self.push(first_elem)

    # Return the number of elements in the stack
    def size(self):
        return len(self.list)

    # Check if the stack is empty
    def is_empty(self):
        return self.size() == 0

    # Push an element on the stack
    def push(self, elem):
        self.list.append(elem)

    # Pop an element off the stack
    # Raises an error if the stack is empty
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.list.pop()

    # Peek the top of the stack without removing the element
    # Raises an error if the stack is empty
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.list[-1]

    # Allow users to iterate through the stack using an iterator
    def __iter__(self):
        self._index = len(self.list)
        return self

    def __next__(self):
        if self._index > 0:
            self._index -= 1
            return self.list[self._index]
        else:
            raise StopIteration


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # 3
    print(stack.peek())  # 2
    print(stack.size())  # 2

    for item in stack:
        print(item)  # 2, 1
