from test_framework import generic_test
from collections import Counter


def can_form_palindrome(s):
    counts = Counter(s)
    odd = 0

    for c in counts:
        if counts[c] % 2 != 0:
            odd += 1

    return odd == 0 or odd == 1 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
