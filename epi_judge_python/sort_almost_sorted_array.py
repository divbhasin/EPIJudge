from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    heap = []
    final = []

    for num in sequence:
        heapq.heappush(heap, num)
        if len(heap) == k + 1:
            top = heapq.heappop(heap)
            final.append(top)

    while heap:
        top = heapq.heappop(heap)
        final.append(top)

    return final 


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
