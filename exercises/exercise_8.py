# Your solution to Exercise 8

userInput = int(input())
checkDigit = int(input())

inDigit = checkDigit == userInput % 10 or checkDigit == (userInput // 10) % 10 or checkDigit == userInput // 100

print(inDigit)
