def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.

    Args:
        nums: List of integers
        target: The target sum

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_dict(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.

    Args:
        nums: List of integers
        target: The target sum

    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    visited = {}
    for i ,number in enumerate(nums):
        complement = target - number
        if complement in visited:
            return [visited[complement],i]
        visited[number] =i


def main()-> None:
    nums= [2, 7, 11, 15]
    print(two_sum(nums,9))
    print(two_sum_dict(nums,9))

if __name__ == "__main__":
    main()
