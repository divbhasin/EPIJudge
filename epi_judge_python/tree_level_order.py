from test_framework import generic_test


def binary_tree_depth_order(tree):
    if tree is None:
        return []

    q = [[tree, 0]]
    res = []

    while len(q) > 0:
        curr, d = q.pop(0)
        if d == len(res):
            res.append([curr.data])
        else:
            res[d].append(curr.data)

        if curr.left:
            q.append([curr.left, d+1])
        if curr.right:
            q.append([curr.right, d+1])

    return res 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
