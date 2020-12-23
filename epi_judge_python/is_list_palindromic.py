from test_framework import generic_test
from list_node import ListNode


def is_linked_list_a_palindrome(L):
    def reverse(head):
        h = ListNode(0, head)
        curr = h.next

        while curr and curr.next:
            t = curr.next

            curr.next = t.next
            t.next = h.next
            h.next = t

        return h.next

    dummy = ListNode(0, L)
    slow, fast = dummy, dummy 
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    rev = reverse(slow.next)
    slow.next = None

    curr = L

    while rev and curr:
        if rev.data != curr.data:
            return False

        rev, curr = rev.next, curr.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
