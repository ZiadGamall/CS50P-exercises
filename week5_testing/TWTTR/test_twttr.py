# Tests the shorten function from twttr.py, ensuring it removes all vowels (case-insensitively).

from twttr import shorten

def test_remove_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_mixed_characters():
    assert shorten("Twitter") == "Twttr"

def test_upper_and_lower_mix():
    assert shorten("ApPlE") == "pPl"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
