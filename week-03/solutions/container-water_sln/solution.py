def maxArea(height: list[int]) -> int:
    """
    Given an array of non-negative integers representing elevation at each position,
    find two lines that, together with the x-axis, form a container with the maximum
    amount of water.

    Args:
        height (list[int]): List of non-negative integers representing heights.

    Returns:
        int: Maximum area of water container.
    """
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_area = max(max_area, area)

        # Move the pointer with smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def main():
    # Test cases
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Expected 49
    print(maxArea([1, 1]))  # Expected 1
    print(maxArea([4, 3, 2, 1, 4]))  # Expected 16


if __name__ == "__main__":
    main()
