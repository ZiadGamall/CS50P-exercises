# Tests the convert function from fuel.py, ensuring correct percentage and E/F results from input fractions.

import pytest
from fuel import convert

def test_full_tank():
    assert convert("1/1") == "F"

def test_empty_tank():
    assert convert("0/100") == "E"

def test_midrange():
    assert convert("3/4") == "75%"

def test_rounding_down():
    assert convert("1/2") == "50%"

def test_invalid_fraction_over_100():
    with pytest.raises(ValueError):
        convert("5/4")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_float_in_fraction():
    with pytest.raises(ValueError):
        convert("1.5/2")
