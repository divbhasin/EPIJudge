import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    def length(head):
        l, curr = 0, head
        while curr:
            curr = curr.next
            l += 1

        return l

    curr0 = l0
    while curr0 and curr0.next:
        curr0 = curr0.next

    curr1 = l1
    while curr1 and curr1.next:
        curr1 = curr1.next

    if curr1 != curr0 or (curr1 == curr0 and curr1 is None):
        return None

    len0 = length(l0)
    len1 = length(l1)

    if len1 > len0:
        l0, l1 = l1, l0

    curr0 = l0
    for _ in range(abs(len0 - len1)):
        curr0 = curr0.next

    curr1 = l1
    while curr1 != curr0:
        curr0 = curr0.next
        curr1 = curr1.next

    return curr0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
