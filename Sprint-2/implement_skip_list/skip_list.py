class SkipList:
    def __init__(self):
        self.items = []

    def insert(self, value):
        left = 0
        right = len(self.items)

        while left < right:
            mid = (left + right) // 2

            if self.items[mid] < value:
                left = mid + 1
            else:
                right = mid

        self.items.insert(left, value)

    def __contains__(self, value):
        left = 0
        right = len(self.items) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.items[mid] == value:
                return True

            if self.items[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def to_list(self):
        return list(self.items)