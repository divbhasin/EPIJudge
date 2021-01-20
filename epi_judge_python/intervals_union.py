import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))

    res = [intervals[0]]

    for i in intervals:
        top = res[-1]
        if (top.right.val > i.left.val) or \
            (top.right.val == i.left.val and \
            (top.right.is_closed or i.left.is_closed)):

            if (top.right.val < i.right.val) or \
                (top.right.val == i.left.val and i.right.is_closed):

                new_int = Interval(top.left, i.right)
                res.pop()
                res.append(new_int)
        else:
            res.append(i)

    return res 


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
