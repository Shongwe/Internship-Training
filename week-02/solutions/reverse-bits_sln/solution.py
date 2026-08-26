def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a 32-bit unsigned integer.

    Args:
        n: A 32-bit unsigned integer.

    Returns:
        The integer obtained by reversing all 32 bits.
    """
    result = 0

    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result


def main():
    n = 43261596
    print("Reversed Bits:", reverse_bits(n))


if __name__ == "__main__":
    main()