import os
import sys

from dataclasses import dataclass
from typing import Dict, Optional

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from implement_linked_list.linked_list import Entry, LinkedList


@dataclass
class KeyValuePair[K, V]:
    key: K
    value: V


class LruCache[K, V]:
    def __init__(self, *, limit: int):
        if limit < 1:
            raise ValueError("limit must be non-negative")
        self.limit = limit
        self.entries: Dict[K, Entry[KeyValuePair[K, V]]] = dict()
        self.list = LinkedList[Entry[KeyValuePair[K, V]]]()

    def get(self, key: K) -> Optional[V]:
        entry = self.entries.get(key)
        if entry is not None:
            self.touch(entry)
            return entry.value.value
        return None

    def set(self, key: K, value: V):
        if len(self.entries) == self.limit:
            popped = self.list.pop_tail()
            del self.entries[popped.key]

        entry = self.entries.get(key)
        if entry is not None:
            entry.value = KeyValuePair(key, value)
            self.touch(entry)
        else:
            entry = self.list.push_head(KeyValuePair(key, value))
            self.entries[key] = entry

    def touch(self, entry: Entry[KeyValuePair[K, V]]):
        self.list.remove(entry)
        self.entries[entry.value.key] = self.list.push_head(entry.value)
