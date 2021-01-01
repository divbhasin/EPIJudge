from test_framework import generic_test


def is_symmetric(tree):
    def check_equal(n1, n2):
        if not n1 and not n2:
            return True
        elif (n1 and not n2) or (n2 and not n1):
            return False

        return n1.data == n2.data and check_equal(n1.left, n2.right) and \
            check_equal(n1.right, n2.left)

    if tree:
        return check_equal(tree.left, tree.right)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
