import unittest
from src.sum import sum

class TestSum(unittest.TestCase):
  def test_sum_integers(self):
    """
    Test that it can sum 2 numbers
    """

    num1 = 10
    num2 = 17
    result = sum(num1, num2)
    self.assertEqual(result, 27)

if __name__ == '__main__':
    unittest.main()
