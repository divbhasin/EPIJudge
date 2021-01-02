from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def helper(preorder, inorder, i_i, i_j, p_i):
    if i_i > i_j:
        return None

    root = BinaryTreeNode(preorder[p_i])
    pos = i_i

    for c in range(i_i+1, i_j+1):
        if inorder[c] == root.data:
            pos = c
            break

    root.left = helper(preorder, inorder, i_i, pos - 1, p_i + 1)
    root.right = helper(preorder, inorder, pos + 1, i_j, p_i + (pos-i_i)+1)

    return root

def binary_tree_from_preorder_inorder(preorder, inorder):
    return helper(preorder, inorder, 0, len(inorder) - 1, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
