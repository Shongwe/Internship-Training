def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place.

    Args:
        nums1: First sorted array with extra space
        m: Number of valid elements in nums1
        nums2: Second sorted array
        n: Number of valid elements in nums2

    Returns:
        None (modifies nums1 in-place)
    """
    # Start from the end of both arrays
    i, j, k = m - 1, n - 1, m + n - 1

    # Merge in reverse order
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


def main() -> None:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
