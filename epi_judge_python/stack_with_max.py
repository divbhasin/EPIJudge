from test_framework import generic_test
from test_framework.test_failure import TestFailure

class ListNode:
    def __init__(self, val=0, next=None, maxv=float('-inf'), prev=None):
        self.val = val
        self.next = next
        self.maxv = maxv
        self.prev = prev

class Stack:
    def __init__(self):
        self.curr = ListNode()
        self.cap = 0

    def empty(self):
        return self.cap == 0

    def max(self):
        if self.cap == 0:
            print("stack is empty!")
            return

        return self.curr.maxv

    def pop(self):
        if self.cap == 0:
            print("stack is empty!")
            return

        self.cap -= 1
        val = self.curr.val
        self.curr = self.curr.prev
        self.curr.next = None
        return val

    def push(self, x):
        self.cap += 1
        new_curr = ListNode()
        new_curr.val = x
        new_curr.prev = self.curr
        new_curr.maxv = max(self.curr.maxv, new_curr.val)
        self.curr.next = new_curr
        self.curr = new_curr


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
