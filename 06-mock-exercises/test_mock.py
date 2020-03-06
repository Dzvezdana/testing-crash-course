import mock
import pandas as pd
from src.main import is_sum_of_series_greather_than_1000000

s1 = pd.Series([1000000, 1000000])
s2 = pd.Series([20, 20])

def test_big():
  assert is_sum_of_series_greather_than_1000000(s1) is True

def test_not_big():
  assert is_sum_of_series_greather_than_1000000(s2) is False
