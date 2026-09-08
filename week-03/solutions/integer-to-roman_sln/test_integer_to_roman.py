from solution import intToRoman


def test_examples():
    assert intToRoman(3) == "III"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"


def test_edge_cases():
    assert intToRoman(1) == "I"
    assert intToRoman(4) == "IV"
    assert intToRoman(9) == "IX"
    assert intToRoman(40) == "XL"
    assert intToRoman(90) == "XC"
    assert intToRoman(400) == "CD"
    assert intToRoman(900) == "CM"
    assert intToRoman(3999) == "MMMCMXCIX"


def test_round_numbers():
    assert intToRoman(5) == "V"
    assert intToRoman(10) == "X"
    assert intToRoman(50) == "L"
    assert intToRoman(100) == "C"
    assert intToRoman(500) == "D"
    assert intToRoman(1000) == "M"


def test_complex_cases():
    assert intToRoman(44) == "XLIV"
    assert intToRoman(99) == "XCIX"
    assert intToRoman(145) == "CXLV"
    assert intToRoman(944) == "CMXLIV"
    assert intToRoman(1987) == "MCMLXXXVII"
    assert intToRoman(2021) == "MMXXI"
