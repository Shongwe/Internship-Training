from solution import next_permutation


def test_next_permutation_basic():
    nums = [1, 2, 3]

    next_permutation(nums)

    assert nums == [1, 3, 2]


def test_next_permutation_descending():
    nums = [3, 2, 1]

    next_permutation(nums)

    assert nums == [1, 2, 3]


def test_next_permutation_duplicates():
    nums = [1, 1, 5]

    next_permutation(nums)

    assert nums == [1, 5, 1]


def test_next_permutation_single_element():
    nums = [1]

    next_permutation(nums)

    assert nums == [1]


def test_next_permutation_two_elements():
    nums = [1, 2]

    next_permutation(nums)

    assert nums == [2, 1]


def test_next_permutation_wrap_around():
    nums = [2, 1]

    next_permutation(nums)

    assert nums == [1, 2]


def test_next_permutation_multiple_duplicates():
    nums = [1, 3, 2, 2]

    next_permutation(nums)

    assert nums == [2, 1, 2, 3]