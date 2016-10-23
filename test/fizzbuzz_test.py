import pytest
import sys
sys.path.append('src/')
from FizzBuzz import FizzBuzz

def test_受け取った数値をそのまま返すこと():
    fizzBuzz = FizzBuzz()

    assert 1 == fizzBuzz.calc(1)
    assert 2 == fizzBuzz.calc(2)

@pytest.mark.parametrize(('arg', 'expected'), [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (6, 'Fizz'),
    (9, 'Fizz'),
    (5, 'Buzz'),
    (10, 'Buzz'),
    (15, 'FizzBuzz'),
    (30, 'FizzBuzz'),
])
def test_受け取った数値をそのまま返すただし３の倍数の場合はFizzを５の倍数の場合はBuzzを３と５両方の倍数の場合にはFizzBuzzを返すこと(arg, expected):
    fizzBuzz = FizzBuzz()

    assert expected == fizzBuzz.calc(arg)
