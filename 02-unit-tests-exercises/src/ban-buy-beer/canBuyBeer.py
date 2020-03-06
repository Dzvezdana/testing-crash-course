import re

def checkId(docnum):
  if not isinstance(docnum, str):
    raise TypeError("Input needs to be a string")
      
  if not re.search(r"^\d+$", docnum):
    raise ValueError("Non-numerical values are not supported")
      
  if len(docnum) != 9:
    return False
  
  return True
