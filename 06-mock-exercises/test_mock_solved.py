import mock
from src.main import is_sum_of_series_greather_than_1000000


def test_big():
  series = mock.Mock()
  series.sum.return_value = 1000001

  assert is_sum_of_series_greather_than_1000000(series) is True

def test_not_big():
  series = mock.Mock()
  series.sum.return_value = 1

  assert is_sum_of_series_greather_than_1000000(series) is False