import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    reverse(s, 0, len(s) - 1)
    start = 0
    for end in range(len(s) + 1):
        if end == len(s) or s[end] == ord(" "):
            reverse(s, start, end - 1)
            start = end + 1

    return s

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
