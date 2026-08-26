def next_permutation(nums: list[int]) -> None:
    """
    Modify nums in-place to produce the next lexicographical permutation.

    Args:
        nums: A list of integers to modify in-place.

    Returns:
        None.
    """
    # Step 1: Find the rightmost position where nums[i] < nums[i + 1].
    i = len(nums) - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the rightmost value greater than nums[i].
        j = len(nums) - 1

        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap the two values.
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix.
    nums[i + 1 :] = reversed(nums[i + 1 :])


def main():
    nums = [1, 2, 3]
    next_permutation(nums)
    print("Next Permutation:", nums)


if __name__ == "__main__":
    main()
