from test_framework import generic_test


def search_smallest(A):
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid > 0 and mid < len(A) - 1 and A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
            return mid
        elif A[hi] > A[mid]:
            hi = mid - 1
        elif A[lo] < A[mid]:
            lo = mid + 1
        else:
            break

    return hi if hi > 0 else lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
