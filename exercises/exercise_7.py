# Your solution to Exercise 7

firstNum = float(input())
secondNum = float(input())
operation = input()

if operation == "+":
  print(firstNum + secondNum)

elif operation == "-":
  print(firstNum - secondNum)

elif operation == "/":
  if secondNum == 0.0:
    print("Division by 0!")

  else:
    print(firstNum / secondNum)

elif operation == "*":
  print(firstNum * secondNum)

elif operation == "mod":
  print(firstNum % secondNum)

elif operation == "pow":
  print(firstNum ** secondNum)

elif operation == "div":
  print(firstNum // secondNum)

else:
  print("Error")
