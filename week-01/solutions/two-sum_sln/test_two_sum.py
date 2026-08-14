from solution import two_sum, two_sum_dict


def test_two_sum_standard_case():
    # Basic example: 2 + 7 = 9
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_unsorted_array():
    # Target is in the middle/end of an unsorted list
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_same_elements():
    # Target made by adding the same number value at different indices
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_negative_numbers():
    # Handles negative integers correctly
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_multiple_possible_pairs():
    # Returns the first valid pair it completes
    # 3 (idx 1) + 4 (idx 2) = 7
    assert two_sum([1, 3, 4, 2], 7) == [1, 2]


def test_two_sum_two_elements():
    # Handles an array containing exactly two elements
    assert two_sum([1, 2], 3) == [0, 1]


def test_two_sum_pair_at_end():
    # Ensures the last element is included in the search
    assert two_sum([1, 2, 3, 4], 7) == [2, 3]


def test_two_sum_does_not_use_same_index():
    # Ensures the same element cannot be used twice
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_dict_standard_case():
    # Basic example: 2 + 7 = 9
    assert two_sum_dict([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_dict_unsorted_array():
    # Target is in the middle/end of an unsorted list
    assert two_sum_dict([3, 2, 4], 6) == [1, 2]


def test_two_sum_dict_same_elements():
    # Handles duplicate values at different indices
    assert two_sum_dict([3, 3], 6) == [0, 1]


def test_two_sum_dict_negative_numbers():
    # Handles negative integers correctly
    assert two_sum_dict([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_two_sum_dict_multiple_possible_pairs():
    # Returns the first valid pair it encounters
    assert two_sum_dict([1, 3, 4, 2], 7) == [1, 2]


def test_two_sum_dict_two_elements():
    # Handles an array containing exactly two elements
    assert two_sum_dict([1, 2], 3) == [0, 1]


def test_two_sum_dict_pair_at_end():
    # Ensures the last element is included in the search
    assert two_sum_dict([1, 2, 3, 4], 7) == [2, 3]


def test_two_sum_dict_does_not_use_same_index():
    # Ensures the same element cannot be used twice
    assert two_sum_dict([3, 2, 4], 6) == [1, 2]