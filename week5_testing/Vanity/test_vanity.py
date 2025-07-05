# Tests the is_valid function from vanity plates, ensuring all plate rules are enforced.

from vanity import is_valid

def test_valid_plate_with_numbers():
    assert is_valid("CS50") == True

def test_too_short_or_long():
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_characters():
    assert is_valid("CS*50") == False
    assert is_valid("PI3.14") == False

def test_number_position_rules():
    assert is_valid("CS05") == False  # starts with 0
    assert is_valid("CS50X") == False  # letter after number
    assert is_valid("CSX50") == True   # number after all letters
