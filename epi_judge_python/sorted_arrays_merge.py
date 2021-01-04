from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    heap = []

    for i in range(len(sorted_arrays)):
        if sorted_arrays[i]:
            heapq.heappush(heap, [sorted_arrays[i][0], 0, i])

    final = []
    while heap:
        elem, idx, arr_num = heapq.heappop(heap)
        if idx < len(sorted_arrays[arr_num]) - 1:
            heapq.heappush(heap, [sorted_arrays[arr_num][idx + 1], idx + 1, arr_num])

        final.append(elem)

    return final

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
