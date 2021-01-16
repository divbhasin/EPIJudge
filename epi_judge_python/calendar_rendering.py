import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    times = []
    for event in A:
        s, f = event.start, event.finish
        times.append((s, True))
        times.append((f, False))

    times.sort(key=lambda x: (x[0], not x[1]))
    count, max_count = 0, 0

    for t in times:
        if t[1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count -= 1

    return max_count


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
