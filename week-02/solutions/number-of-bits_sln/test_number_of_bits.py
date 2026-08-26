from solution import hamming_weight


def test_hamming_weight_example():
    assert hamming_weight(11) == 3


def test_hamming_weight_single_bit():
    assert hamming_weight(128) == 1


def test_hamming_weight_zero():
    assert hamming_weight(0) == 0


def test_hamming_weight_all_32_bits_set():
    assert hamming_weight((1 << 32) - 1) == 32


def test_hamming_weight_power_of_two():
    assert hamming_weight(1) == 1


def test_hamming_weight_multiple_bits():
    assert hamming_weight(15) == 4
