from sum import sum
from subtract import subtract
from multiply import multiply
from divide import divide

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input('Enter one of the above operations: ')

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

if operation == 1:
  print(sum(num1,num2))

if operation == 2:
  print(subtract(num1,num2))

if operation == 3:
  print(multiply(num1,num2))

if operation == 4:
  print(divide(num1,num2))
