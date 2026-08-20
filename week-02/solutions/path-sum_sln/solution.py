class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def hasPathSum(root: Node, targetSum: int) -> bool:
    if not root:
        return False

    # Check if we are at a leaf node
    if not root.left and not root.right:
        return root.value == targetSum

    # Recursively check the left and right subtrees with the updated target sum
    remaining_num = targetSum - root.value
    return hasPathSum(root.left, remaining_num) or hasPathSum(root.right, remaining_num)


def main():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.right = Node(1)

    target_sum = 22
    print(hasPathSum(root, target_sum))


if __name__ == "__main__":
    main()
