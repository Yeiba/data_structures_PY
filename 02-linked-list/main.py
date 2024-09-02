class LinkedList:

    def __init__(self, first_elem=None):
        self.head = self.Node(
            first_elem) if first_elem is not None else first_elem
        self.size = 1 if first_elem is not None else 0
        self.tail = self.head if self.head is not None else None

    class Node:
        def __init__(self, data=None):
            self.data = data  # The value stored in the node
            self.next = None  # Pointer to the next node
    # Append a new node with the given data at the end of the list

    def clear(self):
        trav = self.head
        while trav is not None:
            next_node = trav.next
            trav.next = None
            trav.data = None
            trav = next_node
        self.head = self.tail = trav = None
        self.size = 0

    # Check if the list is empty

    def is_empty(self):
        return self.size == 0

    def Size(self):
        return self.size

    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Link the last node to the new node
        self.size += 1

    # Insert a new node with the given data at the specified index
    def insert(self, data, index):
        try:
            if index < 0:
                raise IndexError("Index out of bounds")

            new_node = self.Node(data)
            if index == 0:
                new_node.next = self.head
                self.head = new_node  # Insert at the beginning
            else:
                current = self.head
                for i in range(index - 1):
                    if current is None:
                        raise IndexError("Index out of bounds")
                    current = current.next

                new_node.next = current.next
                current.next = new_node
            self.size += 1
        except IndexError as e:
            print("Error:", e)

    # Remove a node by value
    def remove(self, data):
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next  # Bypass the current node
                else:
                    self.head = current.next  # Remove the head
                return current.data
            previous = current
            current = current.next
        self.size -= 1

        return None

    # Get the data at the specified index
    def get(self, index):
        try:
            if index < 0:
                raise IndexError("Index out of bounds")

            current = self.head
            count = 0

            while current:
                if count == index:
                    return current.data
                count += 1
                current = current.next

            raise IndexError("Index out of bounds")
        except IndexError as e:
            print("Error:", e)

    # Print the linked list
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    # Get the size of the linked list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.insert(15, 1)
    ll.display()  # Output: [10, 15, 20, 30]

    print(ll.get(2))  # Output: 20
    print('Size:', ll.Size())  # Output: 4
    ll.remove(20)
    ll.display()  # Output: [10, 15, 30]c

    print('Size:', ll.length())  # Output: Size: 3
    print('Is empty:', ll.is_empty())  # Output: Is empty: False
    for i in ll:
        print(i)  # Prints 10, 15, 30

    ll.clear()
    print(ll.Size())  # Output: 0
    print(ll.is_empty())  # true
