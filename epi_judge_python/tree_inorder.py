from test_framework import generic_test


def leaf(node):
    return node.left is None and node.right is None

def inorder_traversal(tree):
    prev, inorder = None, []
    while tree:
        next = None
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                inorder.append(tree.data)
                next = tree.right or tree.parent
        elif prev is tree.left:
            inorder.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent

        prev, tree = tree, next

    return inorder


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
