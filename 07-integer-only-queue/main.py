class IntQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        # One extra space to distinguish full from empty
        self.ar = [0] * (max_size + 1)
        self.front = 0
        self.end = 0

    # Returns true if the queue is empty
    def is_empty(self):
        return self.front == self.end

    # Returns the number of elements inside the queue
    def size(self):
        if self.front > self.end:
            return (self.end + len(self.ar) - self.front)
        return self.end - self.front

    # Peek at the front element without removing it
    def peek(self):
        try:
            if self.is_empty():
                raise IndexError("Queue is empty")
            return self.ar[self.front]
        except IndexError as e:
            print("Error:", e)

    # Add an element to the end of the queue
    def enqueue(self, value):
        try:
            if not isinstance(value, int):
                raise ValueError("Only integers are allowed")
            if (self.end + 1) % len(self.ar) == self.front:
                raise OverflowError("Queue too small!")
            self.ar[self.end] = value
            self.end = (self.end + 1) % len(self.ar)
        except ValueError | OverflowError as e:
            print("Error:", e)

    # Remove and return the element at the front of the queue
    def dequeue(self):
        try:
            if self.is_empty():
                raise IndexError("Queue is empty")
            value = self.ar[self.front]
            self.front = (self.front + 1) % len(self.ar)
            return value
        except IndexError as e:
            print("Error:", e)


# Example usage
if __name__ == "__main__":
    queue = IntQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    print(queue.dequeue())  # Output: 3
    print(queue.dequeue())  # Output: 4

    print(queue.is_empty())  # Output: False

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())  # Output: 5
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    print(queue.dequeue())  # Output: 3

    print(queue.is_empty())  # Output: True
