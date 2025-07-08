# Contains unit tests to verify the correctness of the validate function in numb3rs.py.

from ip_validator import validate

def test_chars():
    assert validate("a.b.c.d") == False
    assert validate("cat") == False
    assert validate("123.222.0.d") == False

def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

def test_invalid():
    assert validate("-1.0.0.0") == False
    assert validate("255.255.255.256") == False
    assert validate("999") == False
    assert validate("123") == False