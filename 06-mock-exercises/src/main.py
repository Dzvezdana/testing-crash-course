"""Check if the datafram is greater than a thousand elements"""
import pandas as pd


def is_sum_of_series_greather_than_1000000(series):
  if series.sum() > 1000000:
    return True
  else:
    return False


if __name__ == "__main__":
  s1 = pd.Series([1000000, 1000000])
  print(s1)
  print(is_sum_of_series_big(s1))

  s2 = pd.Series([1, 1])
  print(s2)
  print(is_sum_of_series_big(s2))
