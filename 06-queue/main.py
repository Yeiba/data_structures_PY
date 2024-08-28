class Queue:
    def __init__(self, first_elem=None):
        self.head = None
        self.tail = None
        self._size = 0

        if first_elem is not None:
            self.offer(first_elem)

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    # Return the size of the queue
    def size(self):
        return self._size

    # Returns whether or not the queue is empty
    def is_empty(self):
        return self._size == 0

    # Peek the element at the front of the queue
    # Raises an error if the queue is empty
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    # Poll an element from the front of the queue
    # Raises an error if the queue is empty
    def poll(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1

        if self.is_empty():
            self.tail = None

        return data

    # Add an element to the back of the queue
    def offer(self, elem):
        new_node = self.Node(elem)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    # Make the queue iterable
    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            data = self._current.data
            self._current = self._current.next
            return data


# Example usage
queue = Queue()

queue.offer(1)
queue.offer(2)
queue.offer(3)

print(queue.peek())  # Output: 1
print(queue.poll())  # Output: 1
print(queue.poll())  # Output: 2
print(queue.poll())  # Output: 3

# Uncomment to test the iterator
# for item in queue:
#     print(item)
