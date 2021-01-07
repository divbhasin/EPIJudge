from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = random.randint(lo, hi)
        pivot = partition(A, lo, hi, mid)
        if pivot + 1 == k:
            return A[pivot]
        elif pivot + 1 > k:
            hi = pivot - 1
        else:
            lo = pivot + 1

    return -1 

def partition(A, lo, hi, mid):
    pivot_val = A[mid]
    new_pivot = lo
    A[hi], A[mid] = A[mid], A[hi]

    for i in range(lo, hi):
        if A[i] > pivot_val:
            A[i], A[new_pivot] = A[new_pivot], A[i]
            new_pivot += 1

    A[new_pivot], A[hi] = A[hi], A[new_pivot]
    return new_pivot

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
