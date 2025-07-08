# Tests the count function from word_counter.py, ensuring it accurately counts full word matches, case-insensitively and safely.

from word_counter import count


def test_basic_cases():
    assert count("hello", "hello world") == 1
    assert count("hello", "HELLO there, hello again") == 2
    assert count("test", "this is a test") == 1


def test_substring_avoidance():
    assert count("he", "hello he hehe") == 1   # only 'he' counts
    assert count("um", "yummy drum um ummm") == 1


def test_special_characters():
    assert count(".", "period . . . end") == 3
    assert count("?", "are you ok? really? what?") == 3
    assert count("C++", "I love C++, but C is okay too.") == 1
