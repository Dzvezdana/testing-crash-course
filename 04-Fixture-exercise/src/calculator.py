import time

class Calculator:

  has_instance = False

  def __init__(self):
    """You should not instatiate more than one Calculator"""
    if self.has_instance is True:
      print("This will take a looong time")
      time.sleep(30)

    self.flag_has_instance()
    return

  @classmethod
  def flag_has_instance(cls):
    cls.has_instance = True

  def sum(self, num1, num2):
    return num1 + num2

  def subtract(self, num1, num2):
    return num1 - num2

  def multiply(self, num1, num2):
    return num1 * num2

  def divide(self, num1, num2):
    return num1 / num2

if __name__ == "__main__":
  print("Using the Calculator only once")
  calc = Calculator()
  print(calc.sum(2, 4))
  print(calc.subtract(4, 2))
  print(calc.multiply(4, 2))
  print(calc.divide(4, 2))
  calc2 = Calculator()
  print(calc2.sum(2, 4))
  print(calc2.subtract(4, 2))
  print(calc2.multiply(4, 2))
  print(calc2.divide(4, 2))
