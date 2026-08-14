from solution import merge


def test_merge_standard_case():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_nums2_empty():
    nums1 = [1]
    nums2 = []

    merge(nums1, 1, nums2, 0)

    assert nums1 == [1]


def test_merge_nums1_empty():
    nums1 = [0]
    nums2 = [1]

    merge(nums1, 0, nums2, 1)

    assert nums1 == [1]


def test_merge_nums2_smaller():
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]

    merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_merge_nums2_larger():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6]

    merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_merge_duplicate_values():
    nums1 = [1, 2, 2, 0, 0, 0]
    nums2 = [2, 2, 3]

    merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 2, 2, 2, 3]


def test_merge_single_elements():
    nums1 = [1, 0]
    nums2 = [2]

    merge(nums1, 1, nums2, 1)

    assert nums1 == [1, 2]


def test_merge_all_nums2_elements_smaller():
    nums1 = [5, 6, 7, 0, 0, 0]
    nums2 = [1, 2, 3]

    merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 3, 5, 6, 7]
