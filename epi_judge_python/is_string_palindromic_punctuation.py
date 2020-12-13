from test_framework import generic_test

def isalphanumeric(c):
    return (ord(c) >= ord('0') and ord(c) <= ord('9')) or \
            (ord(c) >= ord('a') and ord(c) <= ord('z')) or \
            (ord(c) >= ord('A') and ord(c) <= ord('Z'))

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i <= j:
        valid_i, valid_j = isalphanumeric(s[i]), isalphanumeric(s[j])
        if valid_i and valid_j and s[i].lower() != s[j].lower():
            return False
        elif valid_i and valid_j:
            i += 1
            j -= 1

        if not valid_i:
            i += 1
        if not valid_j:
            j -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
