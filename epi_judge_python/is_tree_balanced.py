from test_framework import generic_test


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def is_balanced_binary_tree(tree):
    if not tree:
        return True

    return abs(height(tree.left) - height(tree.right)) <= 1 and \
            is_balanced_binary_tree(tree.left) and \
            is_balanced_binary_tree(tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
