from solution import is_palindrome


def test_valid_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False

    # Edge cases
    assert is_palindrome(" ") is True  # empty after filtering
    assert is_palindrome("0P") is False  # digit + letter mismatch
    assert is_palindrome("No 'x' in Nixon") is True  # mixed case + punctuation
    assert is_palindrome("Able was I, ere I saw Elba") is True  # famous palindrome
    assert is_palindrome("12321") is True  # numeric palindrome
    assert is_palindrome("123ab321") is False  # mixed alphanumeric non-palindrome


def test_single_characters():
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True
    assert is_palindrome("7") is True


def test_empty_string():
    assert is_palindrome("") is True
