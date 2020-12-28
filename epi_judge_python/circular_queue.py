from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.q = [0 for i in range(capacity)]
        self.front, self.back = 0, -1 
        self.curr_len = 0

    def enqueue(self, x):
        if self.curr_len >= len(self.q):
            new_q = [0 for i in range(2 * len(self.q))]
            i = self.front
            for j in range(len(self.q)):
                new_q[j] = self.q[i % len(self.q)]
                i += 1
            self.front, self.back = 0, len(self.q) - 1
            self.q = new_q

        self.back = (self.back + 1) % len(self.q)
        self.q[self.back] = x
        self.curr_len += 1

    def dequeue(self):
        if self.curr_len == 0:
            return

        val = self.q[self.front]
        self.q[self.front] = 0
        self.front = (self.front + 1) % len(self.q)
        self.curr_len -= 1

        return val 

    def size(self):
        return self.curr_len 


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
