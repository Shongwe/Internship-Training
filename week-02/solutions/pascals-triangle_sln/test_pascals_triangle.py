from solution import generate


def test_generate_zero_rows():
    assert generate(0) == []


def test_generate_one_row():
    assert generate(1) == [[1]]


def test_generate_two_rows():
    assert generate(2) == [
        [1],
        [1, 1],
    ]


def test_generate_three_rows():
    assert generate(3) == [
        [1],
        [1, 1],
        [1, 2, 1],
    ]


def test_generate_five_rows():
    assert generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
