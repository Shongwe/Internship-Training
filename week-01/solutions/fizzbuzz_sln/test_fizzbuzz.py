from solution import fizzbuzz

def test_fizzbuzz_15():
    expected_output = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert fizzbuzz(15) == expected_output

def test_fizzbuzz_5():
    expected_output = ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz(5) == expected_output

def test_fizzbuzz_3():
    expected_output = ["1", "2", "Fizz"]
    assert fizzbuzz(3) == expected_output

def test_fizzbuzz_1():
    expected_output = ["1"]
    assert fizzbuzz(1) == expected_output

def test_fizzbuzz_0():
    expected_output = []
    assert fizzbuzz(0) == expected_output

def test_fizzbuzz_negative():
    expected_output = []
    assert fizzbuzz(-5) == expected_output

def test_fizzbuzz_large_number():
    n = 100
    expected_output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            expected_output.append("FizzBuzz")
        elif i % 3 == 0:
            expected_output.append("Fizz")
        elif i % 5 == 0:
            expected_output.append("Buzz")
        else:
            expected_output.append(str(i))
    assert fizzbuzz(n) == expected_output