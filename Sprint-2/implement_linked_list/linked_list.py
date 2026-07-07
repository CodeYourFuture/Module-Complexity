from dataclasses import dataclass
from typing import Any, Optional
# to reduce memory usage we use slots true to tells Python not to create a dynamic __dict__ for every node,
@dataclass(slots=True)
class Node:
    value: Any
    next: Optional['Node'] = None
    previous: Optional['Node'] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def push_head(self, value: Any) -> Node:
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            
        return new_node

    def pop_tail(self) -> Optional[Any]:
        if not self.tail:
            return None
            
        value_to_return = self.tail.value
        self.remove(self.tail)
        return value_to_return

    def remove(self, node_handle: Optional[Node]) -> None:
        if not node_handle:
            return

        if node_handle == self.head:
            self.head = node_handle.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
                
        elif node_handle == self.tail:
            self.tail = node_handle.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
                
        else:
            if node_handle.previous and node_handle.next:
                node_handle.previous.next = node_handle.next
                node_handle.next.previous = node_handle.previous

        node_handle.next = None
        node_handle.previous = None
