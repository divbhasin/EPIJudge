import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    intervals.sort(key=lambda i: i.left)

    res, i = 0, 0

    while i < len(intervals) - 1:
        while i < len(intervals) - 1 and intervals[i].right.val < intervals[i+1].left.val:
            res.append(intervals[i])
            if i == len(intervals) - 2:
                res.append(intervals[i + 1])

            i += 1

        curr = intervals[i]
        while i < len(intervals) - 1 and curr.right.val >= intervals[i+1].left.val:
            i += 1

        new_int = [min(curr.left.val, intervals[i].left.val), \
                max(curr.right.val, intervals[i].right.val)]
        res.append(new_int)

        i += 1

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
