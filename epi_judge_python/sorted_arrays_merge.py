from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    heap = []

    for arr in sorted_arrays:
        for elem in arr:
            heapq.heappush(heap, elem)

    final_arr = []
    while heap:
        min_elem = heapq.heappop(heap)
        final_arr.append(min_elem)

    return final_arr

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
