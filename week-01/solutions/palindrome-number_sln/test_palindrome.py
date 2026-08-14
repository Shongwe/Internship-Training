from solution import is_palindrome


def test_palindrome_standard_case():
    # Basic lower-case odd and even length strings
    assert is_palindrome("racecar") is True
    assert is_palindrome("noon") is True


def test_palindrome_non_palindrome():
    # Standard words that do not match backward
    assert is_palindrome("python") is False
    assert is_palindrome("hello") is False


def test_palindrome_empty_and_single_char():
    # Trivial boundary edge cases
    assert is_palindrome("") is True
    assert is_palindrome("a") is True


def test_palindrome_case_insensitivity():
    # Handles mixed upper and lower case letters
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("AbBa") is True


def test_palindrome_ignores_spaces():
    # Ignores whitespace distribution between letters
    assert is_palindrome("Step on no pets") is True
    assert is_palindrome("Nurses run") is True


def test_palindrome_ignores_punctuation():
    # Strips away non-alphanumeric special characters
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("Madam, I'm Adam.") is True


def test_palindrome_alphanumeric_mixing():
    # Handles numeric digits alongside letters correctly
    assert is_palindrome("12321") is True
    assert is_palindrome("A1b2b1a") is True
    assert is_palindrome("123456") is False
