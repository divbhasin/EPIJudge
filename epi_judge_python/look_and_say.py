from test_framework import generic_test


def look_and_say(n):
    res = "1"
    for i in range(1, n):
        start, curr_res = 1, ""
        while start <= len(res):
            count = 1
            while start > 0 and start < len(res) and res[start] == res[start - 1]:
                count += 1
                start += 1

            curr_res += "{}{}".format(count, res[start - 1])
            start += 1

        res = curr_res

    return res 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
