from test_framework import generic_test


def square_root(k):
    lo, hi = 0, k
    found = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid ** 2 == k:
            return mid
        elif mid ** 2 < k:
            found = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return found 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
