# Tests the get_date and stringify functions from seasons.py, ensuring accurate date parsing and word conversion, with proper error handling and formatting.

import pytest
import datetime
from seasons import stringify, get_date


def test_get_date_valid():
    assert get_date("2000-01-01") == datetime.date(2000, 1, 1)


def test_get_date_invalid(capsys):
    with pytest.raises(SystemExit):
        get_date("not-a-date")
    captured = capsys.readouterr()
    assert "Invalid date" in captured.out


def test_stringify():
    assert stringify(525600) == "Five hundred twenty-five thousand, six hundred"
    assert stringify(1000000) == "One million"
