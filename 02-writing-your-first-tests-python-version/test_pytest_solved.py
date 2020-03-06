import pytest
from src.sum import sum
from src.subtract import subtract
from src.multiply import multiply
from src.divide import divide

class TestSum(object):
  def test_sum_integers(self):

    """
    Test that it can sum 2 numbers
    """
    num1 = 10
    num2 = 17
    result = sum(num1, num2)
    assert result == 27

  def test_sum_negatives(self):
    """
    Test that it can sum negative numbers
    """
    num1 = -10
    num2 = 17
    result = sum(num1, num2)
    assert result == 7

  def test_sum_fractions(self):
    """
    Test that it can sum fractional numbers
    """
    num1 = 1.5
    num2 = 17
    result = sum(num1, num2)
    assert result == 18.5


class TestSubtraction(object):
  def test_subtract_integers(self):
    """
    Test that it can subtract 2 numbers
    """
    num1 = 10
    num2 = 17
    result = subtract(num1, num2)
    assert result == -7

class TestMultiplication(object):
  def test_multiply_integers(self):
    """
    Test that it can multiply 2 numbers
    """
    num1 = 10
    num2 = 17
    result = multiply(num1, num2)
    assert result == 170


class TestDivision(object):
  def test_division(self):

    """
    Test that it can divide 2 numbers
    """
    num1 = 21
    num2 = 7
    result = divide(num1, num2)
    assert result == 3

  def test_raises_an_error_division_by_zero(self):
    """
    Test that it raises an error on division by 0
    """
    num1 = 9
    num2 = 0
    with pytest.raises(ZeroDivisionError):
      result = divide(num1, num2)
