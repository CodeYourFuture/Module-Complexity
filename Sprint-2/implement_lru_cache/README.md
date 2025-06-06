# Implement an LRU cache

Implement a cache in Python with an LRU eviction policy - this means  that if an item needs to be evicted, the item which was least recently used will be evicted. Both setting or getting a value counts as a use.

It should support the following operations. Each operation should have a O(1) worst-case time complexity.

* `LruCache(limit)` should construct an LRU cache which never stores more than `limit` entries.
* `set(key, value)` should associate `value` with the passed `key`.
* `get(key)` should look-up the value previously associated with `key`.

There are some tests in `lru_cache_test.py` for your implementation - feel free to write more.
