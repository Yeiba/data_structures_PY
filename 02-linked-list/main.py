class linked_list:

    class node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = self.node()

    def append(self, data):
        new_node = self.node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    @property
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print('index out of range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print('index out of range')
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


l1 = linked_list()
l1.append(8)
l1.append(7)
l1.append(6)
l1.append(5)


print(l1.get(0))
print(l1.get(1))
print(l1.get(2))
print(l1.get(3))
