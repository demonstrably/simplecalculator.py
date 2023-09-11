#i am trying to make a calculator for simple arithmatic.

num1 = input("what would you like to perform a simple operation on? ")
operator = input("what operation would you like to perform? ")
num2 = input("what other number would you like to perform a simple operation on? ")

addition = int(num1) + int(num2)
multiplication = int(num1) * int(num2)
subtraction = int(num1) - int(num2)
division = int(num1) / int(num2)

if operator == "+" or "adition":
  print("the answer is " + str(addition))
#hooray it works!
if operator == "x" or "*" or "multiplication":
  print("the answer is " str(multiplication))

if operator == "-" or "subtraction" : 
  print("the answer is " str(subtraction))

if operator == "division" or "/" :
  print("the answer is " str(division))

#room for improvement.