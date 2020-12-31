from test_framework import generic_test


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def is_balanced_binary_tree(tree):
    def is_balanced_tree_helper(tree):
        if not tree:
            return (True, -1)

        left_bal, left_height = is_balanced_tree_helper(tree.left)
        if not left_bal:
            return (False, 0)

        right_bal, right_height = is_balanced_tree_helper(tree.right)
        if not right_bal:
            return (False, 0)

        diff = abs(right_height - left_height)
        height = 1 + max(right_height, left_height)
        bal = (diff <= 1)

        return (bal, height)

    return is_balanced_tree_helper(tree)[0]
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
