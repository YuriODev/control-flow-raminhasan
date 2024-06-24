# Your solution to Exercise 9

userInput = int(input())

intSum = (userInput // 100) + (userInput % 10)
midVal = (userInput // 10) % 10

if intSum > midVal:
  print(">")

elif intSum < midVal:
  print("<")

else:
  print("=")
