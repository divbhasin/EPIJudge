from test_framework import generic_test
import bisect


def search_first_of_k(A, k):
    lo, hi = 0, len(A) - 1
    found = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] >= k:
            if A[mid] == k:
                found = mid

            hi = mid - 1
        else:
            lo = mid + 1

    return found 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
