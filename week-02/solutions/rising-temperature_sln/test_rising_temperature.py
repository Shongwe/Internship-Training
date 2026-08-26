from solution import daily_temperatures, daily_temperatures_optimized


def test_daily_temperatures_example():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    expected = [1, 1, 4, 2, 1, 1, 0, 0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_increasing():
    temperatures = [30, 40, 50, 60]
    expected = [1, 1, 1, 0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_increasing_by_thirty():
    temperatures = [30, 60, 90]
    expected = [1, 1, 0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_decreasing():
    temperatures = [90, 80, 70, 60]
    expected = [0, 0, 0, 0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_same_temperature():
    temperatures = [70, 70, 70]
    expected = [0, 0, 0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_single_day():
    temperatures = [75]
    expected = [0]

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected


def test_daily_temperatures_empty():
    temperatures = []
    expected = []

    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_optimized(temperatures) == expected
