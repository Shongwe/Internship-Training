from solution import reverse_bits


def test_reverse_bits_example():
    assert reverse_bits(43261596) == 964176192


def test_reverse_bits_single_bit():
    assert reverse_bits(1) == 2147483648


def test_reverse_bits_zero():
    assert reverse_bits(0) == 0


def test_reverse_bits_all_ones():
    assert reverse_bits(4294967295) == 4294967295


def test_reverse_bits_most_significant_bit():
    assert reverse_bits(2147483648) == 1
