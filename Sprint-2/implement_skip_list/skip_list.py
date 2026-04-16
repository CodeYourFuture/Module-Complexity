import math


class SkipList:
    def __init__(self):
        self.data = []  # sorted list
        self.skips = []  # list of skip pointers, each is a tuple (index, value)

    def rebuild_skips(self):
        """Rebuild the skip pointer so we can jump over sqrt(n) elements."""
        n = len(self.data)
        if n == 0:
            self.skips = []
            return

        step = int(math.sqrt(n)) or 1
        self.skips = list(range(0, n, step))

    def _find_position(self, value):
        """Find the position to insert value using skip pointers."""
        if not self.data:
            return 0

        # Use skip pointers to find the range where value should be
        for i in range(len(self.skips) - 1):
            a = self.skips[i]
            b = self.skips[i + 1]
            if self.data[a] <= value < self.data[b]:
                # linear search between a and b
                for j in range(a, b):
                    if self.data[j] >= value:
                        return j
                return b

        # Check the last skip pointer
        start = self.skips[-1]
        for j in range(start, len(self.data)):
            if self.data[j] >= value:
                return j
        return len(self.data)

    def insert(self, value):
        """Insert value into the skip list, maintaining sorted order."""
        pos = self._find_position(value)

        if pos < len(self.data) and self.data[pos] == value:
            return  # value already exists, do not insert duplicates
        self.data.insert(pos, value)
        self.rebuild_skips()

    def __contains__(self, value):
        if not self.data:
            return False

        for i in range(len(self.skips) - 1):
            a = self.skips[i]
            b = self.skips[i + 1]
            if self.data[a] <= value < self.data[b]:
                return value in self.data[a:b]

        start = self.skips[-1]
        return value in self.data[start::]

    def to_list(self):
        """Return the skip list as a regular sorted list."""
        return self.data
