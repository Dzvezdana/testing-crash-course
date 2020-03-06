import pytest
from src.calculator import Calculator

@pytest.fixture(scope="session")
def calculator_fixture():
  calc = Calculator()
  return calc

def test_sum(calculator_fixture):
  total = calculator_fixture.sum(4, 2)
  assert total == 6

def test_subtract(calculator_fixture):
  total = calculator_fixture.subtract(10, 5)
  assert total == 5

def test_multiply(calculator_fixture):
  total = calculator_fixture.multiply(10, 5)
  assert total == 50

def test_divide(calculator_fixture):
  total = calculator_fixture.divide(10, 5)
  assert total == 2
