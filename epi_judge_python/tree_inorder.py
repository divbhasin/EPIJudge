from test_framework import generic_test


def inorder_traversal(tree):
    def traverse(root, so_far):
        if root is None:
            return

        traverse(root.left, so_far)
        so_far.append(root.data)
        traverse(root.right, so_far)

    inorder = []
    traverse(tree, inorder)
    return inorder 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
