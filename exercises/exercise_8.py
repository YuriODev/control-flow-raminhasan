# Your solution to Exercise 8

userInput = input()

searchList = userInput[0:2]
searchItem = userInput[-1]

if searchItem in searchList:
  print("True")

else:
  print("False")
