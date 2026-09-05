from solution import maxArea


def test_examples():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
    assert maxArea([4, 3, 2, 1, 4]) == 16


def test_edge_cases():
    assert maxArea([5]) == 0
    assert maxArea([5, 5, 5, 5, 5]) == 20
    assert maxArea([1, 2, 3, 4, 5]) == 6
    assert maxArea([5, 4, 3, 2, 1]) == 6


def test_large_values():
    assert maxArea([1000, 1, 1000]) == 2000
    assert maxArea([100, 100, 100, 100]) == 300


def test_varied_patterns():
    assert maxArea([1, 100, 1]) == 2
    assert maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
    assert maxArea([1, 3, 2, 5, 25, 24, 5]) == 24


def test_minimal_cases():
    assert maxArea([]) == 0
    assert maxArea([7, 7]) == 7