import pytest
import sys
sys.path.append('src/')
from FizzBuzz import FizzBuzz

def test_受け取った数値をそのまま返すこと():
    fizzBuzz = FizzBuzz()

    assert 1 == fizzBuzz.calc(1)
    assert 2 == fizzBuzz.calc(2)

def test_３の倍数のときは数の代わりにFizzを返すこと():
    fizzBuzz = FizzBuzz()

    assert 'Fizz' == fizzBuzz.calc(3)
    assert 'Fizz' == fizzBuzz.calc(6)
    assert 'Fizz' == fizzBuzz.calc(9)
