def is_palindrome(x: int) -> bool:
    """
    Determine if an integer is a palindrome.

    Args:
        x: The integer to check

    Returns:
        True if x is a palindrome, False otherwise
    """
    if x < 0:
        return False
    string_x = str(x)
    return string_x == string_x[::-1]


def is_palindromemath(x: int) -> bool:
    if x < 0:
        return False

    init = x
    reverse = 0

    while x > 0:
        last = x % 10
        reverse = (reverse * 10) + last
        x = x // 10
    return init == reverse


def main() -> None:
    print(is_palindrome(110110011011))
    print(is_palindromemath(110110011011))


if __name__ == "__main__":
    main()
