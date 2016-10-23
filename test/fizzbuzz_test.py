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

def test_５の倍数のときは数の代わりにBuzzを返すこと():
    fizzBuzz = FizzBuzz()

    assert 'Buzz' == fizzBuzz.calc(5)
    assert 'Buzz' == fizzBuzz.calc(10)

def test_３と５両方の倍数の場合にはFizzBuzzを返すこと():
    fizzBuzz = FizzBuzz()

    assert 'FizzBuzz' == fizzBuzz.calc(15)
    assert 'FizzBuzz' == fizzBuzz.calc(30)
