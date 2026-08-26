import pytest
from solution import (
    TreeNode,
    preorder_traversal_recursive,
    preorder_traversal_iterative,
)


def build_test_tree():
    # Tree: [1,null,2,3]
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    return root


def test_recursive_preorder():
    root = build_test_tree()
    assert preorder_traversal_recursive(root) == [1, 2, 3]


def test_iterative_preorder():
    root = build_test_tree()
    assert preorder_traversal_iterative(root) == [1, 2, 3]


def test_empty_tree():
    assert preorder_traversal_recursive(None) == []
    assert preorder_traversal_iterative(None) == []


def test_single_node():
    root = TreeNode(42)
    assert preorder_traversal_recursive(root) == [42]
    assert preorder_traversal_iterative(root) == [42]


def build_large_tree():
    # Balanced tree with 7 nodes
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def test_recursive_preorder():
    root = build_test_tree()
    assert preorder_traversal_recursive(root) == [1, 2, 3]


def test_iterative_preorder():
    root = build_test_tree()
    assert preorder_traversal_iterative(root) == [1, 2, 3]


def test_empty_tree():
    assert preorder_traversal_recursive(None) == []
    assert preorder_traversal_iterative(None) == []


def test_single_node():
    root = TreeNode(42)
    assert preorder_traversal_recursive(root) == [42]
    assert preorder_traversal_iterative(root) == [42]


def test_large_tree_recursive():
    root = build_large_tree()
    # Preorder: root -> left -> right
    assert preorder_traversal_recursive(root) == [1, 2, 4, 5, 3, 6, 7]


def test_large_tree_iterative():
    root = build_large_tree()
    assert preorder_traversal_iterative(root) == [1, 2, 4, 5, 3, 6, 7]
