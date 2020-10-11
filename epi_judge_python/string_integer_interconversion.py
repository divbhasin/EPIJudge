from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(num):
    if num == 0:
        return "0"

    ans, sign = [], '+'

    if num < 0:
        sign = '-'
        num = -1 * num

    while num > 0:
        ans.append("{}".format(num % 10))
        num //= 10

    if sign == '-':
        ans.append('-')

    ans.reverse()
    return "".join(ans)


def string_to_int(s):
    if len(s) == 0:
        return

    sign = "+"
    if s[0] == "-":
        sign = "-"

    res = 0
    for c in s:
        if c != "-":
            res = res * 10 + (ord(c) - ord('0'))

    if sign == "-":
        res = 0 - res

    return res

def wrapper(x, s):
    res_x = int_to_string(x)
    if res_x != s:
        print("reached here")
        print(res_x)
        raise TestFailure("Int to string conversion failed")

    res_s = string_to_int(s)
    if res_s != x:
        print(res_s)
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
