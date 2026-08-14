from solution import climb_stairs


def test_climb_stairs_zero():
    # There is one way to reach the ground: take no steps.
    assert climb_stairs(0) == 1


def test_climb_stairs_one():
    # Only one way: 1
    assert climb_stairs(1) == 1


def test_climb_stairs_two():
    # Two ways: 1 + 1, 2
    assert climb_stairs(2) == 2


def test_climb_stairs_three():
    # Three ways: 1 + 1 + 1, 1 + 2, 2 + 1
    assert climb_stairs(3) == 3


def test_climb_stairs_four():
    # Five distinct ways to reach step 4.
    assert climb_stairs(4) == 5


def test_climb_stairs_five():
    assert climb_stairs(5) == 8


def test_climb_stairs_ten():
    assert climb_stairs(10) == 89


def test_climb_stairs_twenty():
    assert climb_stairs(20) == 10946


def test_climb_stairs_large_value():
    # Tests that the iterative solution handles larger inputs efficiently.
    assert climb_stairs(30) == 1346269