from src.sum import sum

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
