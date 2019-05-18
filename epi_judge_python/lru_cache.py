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

[ ATTEMPTED ] 5/18
"""

class LruCache:
    def __init__(self, capacity):
        return

    def lookup(self, isbn):
        pass
    def insert(self, isbn, price):
        pass

    def erase(self, isbn):
        pass




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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
