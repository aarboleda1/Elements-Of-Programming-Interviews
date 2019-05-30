"""
Iterate over a singly linked list backwards. Call print on each node.

This question is aimed at covering a breadth of topics from recursion to
knowledge of data structures, memory allocation in the stack, pointer
"""

class ListNode:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data
"""1 -> 2 -> 3
None
3
2
1
"""
"""This should be done in a few minutes.

Key points:
- After coding is complete transition to asking why a recursive solution is not
great. You are looking to see if the candidate knows what stack overflow is and
how aware s/he is of the amount of stack space allocated to each thread. Does
s/he know the difference between stack and heap ? Then ask about the amount
of space used on the stack for each functions frame and see if they can account
for major parts:

https://wiki.osdev.org/Stack
"""
def iterateBackwardsRecursive(L):
    if not L:
        return

    iterateBackwardsRecursive(L.next)
    print(L.data)
"""Key points
- Familiarity of data structures LIFO and FIFO.
- Array requires reallocation but has great locality of reference and no space
overhead.
- Linked list has no reallocation overhead but has poor memory locality and uses
at least two machine sized words per node in the original list.
At this point, ask the candidate to combine the two solutions to eliminate the
weaknesses. The answer you are looking for is a bucket allocator that uses N-1
slots for data and the last slot for the pointer to the next bucket. Then talk
about the right bucket size given completely random distribution of input lengths.
You are looking to see if the candidate is aware of concept of pages and how OS
gives memory to applications. If the candidate is particularly strong you can
continue with a discussion of heap allocators and trade offs with different
algorithms with respect to fragmentation vs allocation speed. If the candidate
has the right background, you can discuss GCs and different GC algorithms and
whether that affects the design.
"""
def iterateBackwardsIterative(L):
    stack = []
    cur = L
    while cur:
        stack.append(cur)
        cur = cur.next

    while stack:
        node = stack.pop()
        print(node.data)

def iterateBackwardsByReversingInPlace(L):
    if not L:
        return L
    cur = L
    prev = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    cur = prev
    while cur:
        print(cur.data)
        cur = cur.next
# Uses O(N ^ 2) time complexity
def iterateBackwardsWithO1Memory(L):
    last = None
    while last != L:
        cur = L
        while cur.next != last:
            cur = cur.next
        print(cur.data)
        last = cur



if __name__ == "__main__":
    L = ListNode(1, ListNode(2, ListNode(3)))
    # iterateBackwardsRecursive(L)
    # iterateBackwardsIterative(L)
    # iterateBackwardsByReversingInPlace(L)
    iterateBackwardsWithO1Memory(L)
