def hamming_weight(n: int) -> int:
    """
    Return the number of 1 bits in an unsigned integer.

    Args:
        n: An unsigned integer.

    Returns:
        The number of set bits in n.
    """
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count


def main():
    numbers = [11, 128, 0, (1 << 32) - 1]

    for number in numbers:
        print(f"Number: {number}, 1 bits: {hamming_weight(number)}")


if __name__ == "__main__":
    main()