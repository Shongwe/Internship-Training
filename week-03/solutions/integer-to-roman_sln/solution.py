def intToRoman(num: int) -> str:
    """
    Convert an integer to its Roman numeral representation.

    Args:
        num (int): Integer between 1 and 3999.

    Returns:
        str: Roman numeral string.
    """
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, symbol in values:
        count = num // value
        if count:
            result += symbol * count
            num -= value * count

    return result


def main() -> None:
    print(intToRoman(3))  # Expected "III"
    print(intToRoman(58))  # Expected "LVIII"
    print(intToRoman(1994))  # Expected "MCMXCIV"


if __name__ == "__main__":
    main()
