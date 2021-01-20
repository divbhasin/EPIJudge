from test_framework import generic_test


def inorder(root, inord):
    if not root:
        return

    inorder(root.left, inord)
    inord.append(root.data)
    inorder(root.right, inord)

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    inord = []
    inorder(tree, inord)

    for i in range(1, len(inord)):
        if inord[i] < inord[i - 1]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
