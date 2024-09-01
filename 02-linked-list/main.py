class LinkedList:

    def __init__(self, firstNode=None):
        if firstNode is not None:   # The first node in the list
            self.head = self.Node(firstNode)
        else:
            self.head = None

    class Node:
        def __init__(self, data=None):
            self.data = data  # The value stored in the node
            self.next = None  # Pointer to the next node
    # Append a new node with the given data at the end of the list

    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Link the last node to the new node

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

    # Check if the list is empty
    def is_empty(self):
        return self.head is None


# Example usage:
if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.insert(15, 1)
    ll.display()  # Output: [10, 15, 20, 30]

    print(ll.get(2))  # Output: 20

    ll.remove(20)
    ll.display()  # Output: [10, 15, 30]

    print('Size:', ll.length())  # Output: Size: 3
    print('Is empty:', ll.is_empty())  # Output: Is empty: False
