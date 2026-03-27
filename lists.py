class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_values = [str(last.value)]

            while last.next:
                last = last.next
                return_values.append(str(last.value))
            
            return ', '.join(return_values)

    # O(n)
    def __contains__(self, item):
        last = self.head
        while last is not None:
            if last.value == item:
                return True
            last = last.next
        return False

    # O(n)
    def __len__(self):
        last = self.head
        count = 0
        while last is not None:
            count += 1
            last = last.next
        return count

    # O(1)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1)
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    # O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for _ in range(index-1):
                    if last.next is None:
                        raise ValueError('Index out of bounds')
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n)
    def delete(self, value):
        last = self.head

        if last is not None:
            if last.value == value:
                last = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O (n)
    def pop(self, index):
        if self.head is None:
            raise ValueError('Index out of bounds')
        else:
            last = self.head
            for _ in range(index-1):
                if last.next is None:
                    raise ValueError('Index out of bounds')
                last = last.next
            if last.next is None:
                raise ValueError('Index out of bounds')
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # O(n)
    def get(self, index):
        if self.head is None:
            raise ValueError('Index out of bounds')
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError('Index out of bounds')
                last = last.next
            return last.value

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.prepend(2)
    l.insert(3, 1)
    print(l.get(1))
    l.pop(1)
    l.delete(1)
    print(l)