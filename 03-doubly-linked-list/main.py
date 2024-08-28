class DoublyLinkedList:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        trav = self.head
        while trav is not None:
            next_node = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next_node
        self.head = self.tail = trav = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, elem):
        self.add_last(elem)

    def add_last(self, elem):
        if self.is_empty():
            self.head = self.tail = self.Node(elem)
        else:
            self.tail.next = self.Node(elem, self.tail)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        if self.is_empty():
            self.head = self.tail = self.Node(elem)
        else:
            self.head.prev = self.Node(elem, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise ValueError("Empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise ValueError("Empty list")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise ValueError("Empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise ValueError("Empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def remove(self, node):
        if node.prev is None:
            return self.remove_first()
        if node.next is None:
            return self.remove_last()
        node.prev.next = node.next
        node.next.prev = node.prev
        data = node.data
        node.data = None
        node.prev = node.next = None
        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds")
        trav = None
        if index < self.size / 2:
            trav = self.head
            for i in range(index):
                trav = trav.next
        else:
            trav = self.tail
            for i in range(self.size - 1, index, -1):
                trav = trav.prev
        return self.remove(trav)

    def remove_value(self, obj):
        trav = self.head
        while trav is not None:
            if (obj is None and trav.data is None) or (obj is not None and obj == trav.data):
                self.remove(trav)
                return True
            trav = trav.next
        return False

    def index_of(self, obj):
        index = 0
        trav = self.head
        while trav is not None:
            if (obj is None and trav.data is None) or (obj is not None and obj == trav.data):
                return index
            trav = trav.next
            index += 1
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def __iter__(self):
        trav = self.head
        while trav is not None:
            yield trav.data
            trav = trav.next

    def __str__(self):
        sb = "[ "
        trav = self.head
        while trav is not None:
            sb += str(trav.data) + ", "
            trav = trav.next
        sb += " ]"
        return sb


# Example usage:
dll = DoublyLinkedList()
dll.add(3)
dll.add_first(2)
dll.add_last(4)

print(dll)  # [ 2, 3, 4, ]

print(dll.peek_first())  # 2
print(dll.peek_last())   # 4

dll.remove_first()
dll.remove_last()

print(dll)  # [ 3, ]

dll.add(5)
dll.add(6)
dll.add(7)

print(dll.remove_at(1))  # 6
print(dll)  # [ 3, 7, ]

print(dll.index_of(7))  # 1
print(dll.contains(5))  # False
