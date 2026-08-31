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