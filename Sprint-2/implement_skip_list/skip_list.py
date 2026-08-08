import math


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SkipList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.skips = []  # list of skip pointers, each is a tuple (index, value)

    def _get_node(self, index):
        """Get the node at the given index."""
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def rebuild_skips(self):
        """Rebuild the skip pointer so we can jump over sqrt(n) elements."""
        n = self.length
        if n == 0:
            self.skips = []
            return

        step = int(math.sqrt(n)) or 1
        self.skips = list(range(0, n, step))

    def _find_position(self, value):
        """Find the position to insert value using skip pointers."""
        if self.length == 0:
            return 0

        # Use skip pointers to find the range where value should be
        for i in range(len(self.skips) - 1):
            a = self.skips[i]
            b = self.skips[i + 1]

            node_a = self._get_node(a)
            node_b = self._get_node(b)

            if node_a.value <= value < node_b.value:
                # linear search between a and b
                idx = a
                current = node_a
                while idx < b and current:
                    if current.value >= value:
                        return idx
                    current = current.next
                    idx += 1
                return b
        # Check the last skip pointer
        start = self.skips[-1]
        idx = start
        current = self._get_node(start)
        while current:
            if current.value >= value:
                return idx
            current = current.next
            idx += 1
        return self.length

    def insert(self, value):
        """Insert value into the skip list, maintaining sorted order."""
        pos = self._find_position(value)

        if pos < self.length:
            node_at_pos = self._get_node(pos)
            if node_at_pos and node_at_pos.value == value:
                return  # value already exists, do not insert duplicates
        # Insert the new node
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self._get_node(pos - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length += 1
        self.rebuild_skips()

    def __contains__(self, value):
        if self.length == 0:
            return False

        for i in range(len(self.skips) - 1):
            a = self.skips[i]
            b = self.skips[i + 1]

            node_a = self._get_node(a)
            node_b = self._get_node(b)

            if node_a.value <= value < node_b.value:
                idx = a
                current = node_a
                while idx < b and current:
                    if current.value == value:
                        return True
                    current = current.next
                    idx += 1
                return False
        start = self.skips[-1]
        idx = start
        current = self._get_node(start)

        while current:
            if current.value == value:
                return True
            current = current.next
            idx += 1

        return False

    def to_list(self):
        """Return the skip list as a regular sorted list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
