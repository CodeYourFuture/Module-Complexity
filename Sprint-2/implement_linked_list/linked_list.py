from dataclasses import dataclass
from typing import Optional

@dataclass
class Entry[V]:
    value: V
    next: "Optional[Entry[V]]" = None
    previous: "Optional[Entry[V]]" = None


class LinkedList[V]:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value: V) -> Entry[V]:
        old_head = self.head
        entry = Entry(value=value, next=self.head)
        self.head = entry
        if old_head:
            old_head.previous = entry
        if self.tail is None:
            self.tail = entry
        return entry

    def pop_tail(self) -> V:
        tail = self.tail
        self.remove(self.tail)
        return tail.value

    def remove(self, entry: Entry[V]):
        if entry.next:
            entry.next.previous = entry.previous
        if entry.previous:
            entry.previous.next = entry.next
        if self.head == entry:
            self.head = entry.next
        if self.tail == entry:
            self.tail = entry.previous
