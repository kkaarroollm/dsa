class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, data):  # O(n)
        node = Node(data=data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self._length += 1

    def prepend(self, data):  # O(1)
        node = Node(data=data)
        node.next = self.head
        self.head = node
        self._length += 1

    def get(self, index):  # O(n)
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def insert(self, index, data):
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._length += 1

    def remove(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._length -= 1

    def __str__(self):
        return "head -> " + " -> ".join(f"[{data}]" for data in self)


ll = LinkedList()
ll.prepend(2)
ll.prepend(3)
ll.prepend(5)
ll.prepend(1)

ll.append(12)
ll.append(10)

print(ll.get(5))
print(ll.get(4))
print(ll.get(0))

ll.insert(4, 69)
ll.insert(2 ,42)

ll.remove(5)

print(ll)
