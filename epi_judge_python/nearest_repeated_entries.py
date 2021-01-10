from test_framework import generic_test


def find_nearest_repetition(paragraph):
    words, lowest_dist = {}, float('inf')

    for i in range(len(paragraph)):
        w = paragraph[i]
        if w in words:
            lowest_dist = min(lowest_dist, i - words[w])
        words[w] = i

    return lowest_dist if lowest_dist < float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
