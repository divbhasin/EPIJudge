from test_framework import generic_test


def evaluate(expression):
    exprs = expression.split(",")
    s = []

    for sym in exprs:
        if len(s) > 1 and sym in ["+", "-", "*", "/"]:
            x, y = s.pop(), s.pop()
            if sym == "+":
                s.append(x + y)
            elif sym == "-":
                s.append(y - x)
            elif sym == "*":
                s.append(x * y)
            else: 
                s.append(y // x)
        else:
            s.append(int(sym))

    return s.pop() 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
