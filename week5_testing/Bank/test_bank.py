# Tests the value function from bank.py, ensuring correct reward based on greeting start.

from bank import value

def test_exact_hello():
    assert value("hello") == "$0"

def test_hello_with_spaces_and_caps():
    assert value("   HeLLo there") == "$0"

def test_h_but_not_hello():
    assert value("hi there") == "$20"

def test_different_greeting():
    assert value("good morning") == "$100"
