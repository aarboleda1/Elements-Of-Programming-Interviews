"""

Design a Cache system
Overall strategy: https://github.com/karlseguin/ccache
Concurrency using a Window and other techniques:
    https://openmymind.net/High-Concurrency-LRU-Caching/

Basic Implementation:
    Use LRU methodolgy
    2 data structures
    1) A hash table
        - lookups

    2) A linked list
        - evicting
    New items will be appended to the head of the list.
    Retrieved items will be appended to the list
        Car
            id: 1
            key: 'a'
        {a: Node(1)}
        Cache(max_size=4)
        10 -> 1 -> 4 -> 5

    Items that need to be eviceted will be removed from the tail of the list



Scalability:
    Concurrency
Key components
Eviction
Read
Concurrency

Storage, using a hash table
An LRU algorithm to evict from the cache

- Concurrency
    Use a "Window" object. The point of this is to "limit" how often we
    promote a single item.

    In other words, if an item was recently promoted, it's probably near enough
    the front of the list, so we probably don't need to re-promote it. It works
    well for high concurrency



- Good data structure for this would be a hash table
    - good for lookups amortized O(1)
Item:
    Represents an item in our cache
    key
    value
    promoted_time: # the last time it was promoted

class LinkedList:
    def promote_item_to_front(item: Item, window: Window):
        now = time.now()
        stale = now - window.value

        if item.promoted_time < stale:
            # exit early and don't promote
            return
        self._move_to_front(item)



    def remove_from_tail():
        pass
Cache:
    def __init__(self):
        self.lookup = HashTableWithLock()
        self.window = Window
        self.linked_list = LinkedList()

    def get(key: Key):
        self.lookup.readLock()
        res = self.lookup.get(key)
        if res is None:
            return None
        return res.value
    def set(key: Key, val: Value):
        self.lookup.lock()
        self.


    def set():

"""
