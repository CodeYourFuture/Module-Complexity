from typing import Optional, Iterator


class Node:

    def __init__(self, value):
        self.value = value
        self.next: Optional["Node"] = None
        self.previous: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def push_head(self, value) -> Node:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("pop_tail from empty linked list")

        value = self.tail.value
        self.remove(self.tail)  
        return value

    def remove(self, node: Node):
        if node is None:
            raise ValueError("Cannot remove None node")

        if node == self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
        elif node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = None
        node.previous = None

    def __iter__(self) -> Iterator:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return f"LinkedList([{', '.join(str(v) for v in self)}])"