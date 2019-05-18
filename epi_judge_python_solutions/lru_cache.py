import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""12.3 Implement an ISBN cache
The International Standard Book Number (ISBN) is a unique commerical book
identifier. It is a string of length 10. The first 9 characters are digits; the
last character is a check character. The check character is the sum of the first
9 digits, mod 11, with 10 represented by 'X'. (Modern ISBNs use 13 digits, and
the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.)

Create a cache for lookuping up prices of books identified by their ISBN. For
the purpose of this exercise, treat ISBNs and prices as positive integers. You
must implement lookup, insert, and erase methods. Use the LRU policy for cache
eviction

- Insert: if an ISBN is already present, it should not update the price, but
should update that ISBN to be the most recently used entry
- Lookup: given an ISBN, return the corresponding price; if the element is not
present, return -1. If the ISBN is present, update that entry to be the most
recently used ISBN.
- Erase: remove the specified ISBN and corresponding value from the case. Return
true if the ISBN was present; otherwise, return false

SOLUTION: My intuition was correct in implementing an LRU, but it was overkill.
The recommended solution uses an OrderedDict. The reason is that the OrderedDict
rembers insertion order. So upon insertion, you pop from the dict, and then
re-add it when keeps it in sorted order. It handles the ordering for you

[ ATTEMPTED ] 5/18

"""
class LruCache:
    def __init__(self, capacity):

        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):

        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):

        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            '''popitem() -> (k, v), return and remove a (key, value) pair.
            Pairs are returned in LIFO order if last is true or FIFO order if false.
            '''
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):

        return self._isbn_price_table.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])

# 5/18 SOLUTION, Passes only 5 / 101 test cases
class DLLNode:
    def __init__(self, key, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.data = data

class LruCache:
    def __init__(self, capacity):
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup_table = {}
        self.capacity = capacity
        self.count = 0
        return

    def lookup(self, isbn):
        if isbn not in self.lookup_table:
            return -1
        node = self.lookup_table[isbn]
        self._move_to_front(node)
        return node.data

    def insert(self, isbn, price):
        if isbn not in self.lookup_table:
            self.lookup_table[isbn] = DLLNode(isbn, price)
            self.count += 1
            if self.count > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.lookup_table[lru_node.key]
        node = self.lookup_table[isbn]
        self._move_to_front(node)
        return node.data

    def erase(self, isbn):
        if isbn not in self.lookup_table:
            return False
        self.count -= 1
        self._remove(self.lookup_table[isbn])
        del self.lookup_table[isbn]
        return True

    def _move_to_front(self, node):
        cur_head = self.head
        node.next = cur_head.next

        # node
        cur_head.next.prev = node
        cur_head.next = node
        return

    def _remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
