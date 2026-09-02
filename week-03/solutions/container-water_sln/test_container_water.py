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
