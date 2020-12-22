from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy = ListNode(0, L)

    i, j = dummy, dummy
    while k > 0:
        k -= 1
        j = j.next

    prev = dummy

    while j:
        prev = i
        i = i.next
        j = j.next

    prev.next = i.next
    i.next = None

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
