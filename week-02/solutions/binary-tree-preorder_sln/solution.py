class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal_recursive(root: TreeNode) -> list[int]:
    """
    Preorder traversal (root -> left -> right) using recursion.
    """
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def preorder_traversal_iterative(root: TreeNode) -> list[int]:
    """
    Preorder traversal (root -> left -> right) using a stack.
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print("Recursive Preorder Traversal:", preorder_traversal_recursive(root))
    print("Iterative Preorder Traversal:", preorder_traversal_iterative(root))


if __name__ == "__main__":
    main()
