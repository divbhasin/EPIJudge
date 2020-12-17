from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    curr1, curr2, dum = L1, L2, ListNode()
    tail = dum

    while curr1 and curr2:
        if curr1.data < curr2.data:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    tail.next = curr1 if curr2 is None else curr2
    return dum.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
