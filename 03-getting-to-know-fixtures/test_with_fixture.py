import pytest

# Python relative import
from src.superPowerfullDataProcessor import data_processor

@pytest.fixture(scope="session")
def result_fixture():
  result = data_processor()
  return result

def test_not_the_correct_matrix(result_fixture):
  assert result_fixture != [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def test_object_type(result_fixture):
  assert isinstance(result_fixture, list)

def test_is_correct_matrix(result_fixture):
  assert result_fixture == [[0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1]]
