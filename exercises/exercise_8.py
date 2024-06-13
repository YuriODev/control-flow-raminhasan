# Your solution to Exercise 8

userInput = input()

searchList = userInput[0:3]
searchItem = userInput[-1]

print(searchList, searchItem)

if searchItem in searchList:
  print("True")

else:
  print("False")
