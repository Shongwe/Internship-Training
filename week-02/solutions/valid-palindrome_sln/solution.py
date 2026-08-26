def is_palindrome(s: str) -> bool:
    """
    Check if a string is a valid palindrome,
    considering only alphanumeric characters and ignoring case.
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def main():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
    ]

    for s, expected in test_cases:
        result = is_palindrome(s)
        assert (
            result == expected
        ), f"Test failed for input: {s}. Expected: {expected}, Got: {result}"
        print(f"Test passed for input: {s}")


if __name__ == "__main__":
    main()
