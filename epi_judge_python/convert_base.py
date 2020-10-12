from test_framework import generic_test

def convert_base(s, b1, b2):
    if s == "0" or s == "-0":
        return s

    base_ten = 0
    for i in range(len(s)):
        if s[i] != "-":
            digit = s[i]
            if digit.isalpha():
                digit = 10 + ord(s[i]) - ord("A")

            base_ten = base_ten * b1 + int(digit)

    res = []
    while base_ten != 0:
        digit = base_ten % b2
        if digit >= 10:
            digit = chr(ord("A") + (digit % 10))

        res.append("{}".format(digit))
        base_ten //= b2

    if s[0] == "-":
        res.append("-")

    return "".join(reversed(res))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
