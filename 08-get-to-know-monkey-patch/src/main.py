import pandas as pd

def load_data_frame_from_sql_and_add_2():
  """This method reads something in a database and 
     makes a complex data transformation"""

  dataframe = pd.read_sql("MyTable", "Conn")

  new_dataframe = dataframe + 2
  return new_dataframe

def complex_data_transformation(dataframe):
  return df + 2
  