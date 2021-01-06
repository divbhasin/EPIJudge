from test_framework import generic_test
import bisect


def search_first_of_k(A, k):
    lo, hi = 0, len(A) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] > k:
            hi = mid - 1
        elif A[mid] < k:
            lo = mid + 1
        elif mid > 0 and A[mid] == k and A[mid - 1] == k:
            lo, hi = mid - 1, mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
