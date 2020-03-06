import pytest

# Python relative import
from src.superPowerfullDataProcessor import data_processor

def test_not_the_correct_matrix():
  result = data_processor()
  assert result != [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def test_object_type():
  result = data_processor()
  assert isinstance(result, list)

def test_is_correct_matrix():
  result = data_processor()
  assert result == [[0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1]]
