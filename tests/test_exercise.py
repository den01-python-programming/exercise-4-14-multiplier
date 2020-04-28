import pytest
from src.multiplier import Multiplier

def test_exercise(capsys):
    multiply_by_three = Multiplier(3)

    assert multiply_by_three.multiply(2) == 6
    assert multiply_by_three.multiply(3) == 9

    multiply_by_three = Multiplier(4)

    assert multiply_by_three.multiply(3) == 12
