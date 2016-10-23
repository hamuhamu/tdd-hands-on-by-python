import pytest
import sys
sys.path.append('src/')
from FizzBuzz import FizzBuzz

def test_受け取った数値をそのまま返すこと():
    fizzBuzz = FizzBuzz()

    assert 1 == fizzBuzz.calc(1)
