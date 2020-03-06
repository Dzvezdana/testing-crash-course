import mock
from src.main import is_this_a_big_datamodel

def test_big():
  dataframe = mock.Mock()
  dataframe.shape = (2000000, 1)

  assert is_this_a_big_datamodel(dataframe) is True


def test_not_big():
  dataframe = mock.Mock()
  dataframe.shape = (100, 1)

  assert is_this_a_big_datamodel(dataframe) is False
