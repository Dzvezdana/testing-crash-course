import pytest
from src import main
import pandas as pd

@pytest.mark.skip
def test_dataframe_add():
  new_dataframe = main.load_data_frame_from_sql_and_add_2()
  assert new_dataframe is not None

def test_dataframe_add_again(monkeypatch):
  def return_dataframe(db, conn):
    return pd.DataFrame([1, 2])

  monkeypatch.setattr(main.pd, "read_sql", return_dataframe)
  new_dataframe = main.load_data_frame_from_sql_and_add_2()

  assert new_dataframe is not None
