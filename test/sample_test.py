from src.sample import Sample
import pytest
import sys


def test_１件テストできること():
    sample = Sample();

    assert 8 == sample.calc(2, 4)

@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (4, 3, 12),
    (3, 2, 6),
    (22, 2, 44),
])
def test_複数件テストできること(x, y, expected):
    sample = Sample();

    assert sample.calc(x, y) == expected
