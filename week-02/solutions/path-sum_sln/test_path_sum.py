# test_path_sum.py
from solution import Node, hasPathSum


def build_test_tree():
    # Build tree: [5,4,8,11,null,13,4,7,2,null,1]
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)

    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)

    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.right = Node(1)

    return root


def test_path_sum_true():
    root = build_test_tree()
    assert hasPathSum(root, 22) is True


def test_path_sum_false():
    root = build_test_tree()
    assert hasPathSum(root, 23) is False


def test_single_node():
    single = Node(1)
    assert hasPathSum(single, 1) is True
    assert hasPathSum(single, 2) is False
