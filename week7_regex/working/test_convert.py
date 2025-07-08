# Tests the convert function from working.py, ensuring correct 24-hour conversion and error handling for invalid input.

from convert import convert
import pytest


def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1:30 PM to 2:45 AM") == "13:30 to 02:45"


def test_missing_minutes():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:59 AM to 12 PM") == "11:59 to 12:00"
    assert convert("12 PM to 12:01 AM") == "12:00 to 00:01"


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:75 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("noon to evening")
