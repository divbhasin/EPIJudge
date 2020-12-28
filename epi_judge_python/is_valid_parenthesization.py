from test_framework import generic_test


def is_well_formed(s):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}

    for c in s:
        if c == '{' or c == '(' or c == '[':
            stack.append(c)
        elif len(stack) == 0 or stack.pop() != pairs[c]:
            return False

    return len(stack) == 0 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
