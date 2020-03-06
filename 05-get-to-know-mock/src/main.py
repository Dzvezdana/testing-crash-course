def is_this_a_big_datamodel(model):

  # Checks if the received model has more than one million entries
  if model.shape[0] > 1000000:
    return True
  else:
    return False