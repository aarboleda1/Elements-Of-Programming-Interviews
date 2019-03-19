from test_framework import generic_test


class Queue:
    def __init__(self):
        self._enq = []
        self._deq = []

    # Takes O(1) time because stack append is O(1)
    def enqueue(self, x):
        self._enq.append(x)

    # Takes O(n) time where n is # of elements in the queue class
    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        if not self._deq:
            raise IndexError('Empty Queue')
        return self._deq.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
