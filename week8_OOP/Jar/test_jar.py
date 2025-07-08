# Tests core functionality of the Jar class, including deposit, withdraw, string representation, and input validation.

from jar import Jar
import pytest

def test_default_and_custom_capacity():
    assert Jar().capacity == 12
    assert Jar(5).capacity == 5

def test_deposit_and_str():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

def test_withdraw():
    jar = Jar(4)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

def test_overflow_and_underflow():
    jar = Jar(2)
    with pytest.raises(ValueError):
        jar.deposit(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Jar(-1)

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
