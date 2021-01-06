from test_framework import generic_test
import bisect


def search_first_of_k(A, k):
    i = bisect.bisect_left(A, k)
    if i >= 0 and i < len(A) and A[i] == k:
        return i

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
