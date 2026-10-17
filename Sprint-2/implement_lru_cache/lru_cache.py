from linked_list import LinkedList


class _CacheEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")

        self.limit = limit
        self.cache = {}
        self.order = LinkedList()

    def get(self, key):
        node = self.cache.get(key)
        if node is None:
            return None

        self.order.remove(node)
        self.cache[key] = self.order.push_head(node.value)
        return node.value.value

    def set(self, key, value):
        node = self.cache.get(key)
        if node is not None:
            node.value.value = value
            self.order.remove(node)
            self.cache[key] = self.order.push_head(node.value)
            return

        entry = _CacheEntry(key, value)
        self.cache[key] = self.order.push_head(entry)

        if len(self.cache) > self.limit:
            least_recently_used = self.order.pop_tail()
            del self.cache[least_recently_used.key]
