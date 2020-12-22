from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    even, odd = ListNode(), ListNode()
    oddHead, evenHead = odd, even

    curr, pos = L, 0

    while curr:
        if pos % 2 == 0:
            even.next = curr
            even = even.next
        else:
            odd.next = curr 
            odd = odd.next

        curr = curr.next
        pos += 1

    odd.next = None
    even.next = oddHead.next
    return evenHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
