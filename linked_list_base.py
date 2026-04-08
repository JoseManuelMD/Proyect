class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
