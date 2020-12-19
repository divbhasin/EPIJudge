from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    dummy = ListNode()
    dummy.next = L

    pos, prev, curr = 0, None, dummy 
    while pos < start:
        prev = curr
        curr = curr.next
        pos += 1

    prevStart, startN = prev, curr

    while pos < finish + 1:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
        pos += 1

    if prevStart and prevStart != prev:
        prevStart.next = prev

    if startN and startN != curr:
        startN.next = curr

    return dummy.next 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
