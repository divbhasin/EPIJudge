from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    dummy = ListNode(0, L)
    sb_head = dummy

    for _ in range(1, start):
        sb_head = sb_head.next

    sub_curr = sb_head.next
    for _ in range(finish - start):
        t = sub_curr.next

        sub_curr.next = t.next
        t.next = sb_head.next
        sb_head.next = t

    return dummy.next 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
