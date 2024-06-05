# Your solution to Exercise 4

userInput = int(input("Enter your grade: "))

output = ''
if 1 <= userInput <= 3:
  output = 'initital level'

elif 4 <= userInput <= 6:
  output = 'average level'

elif 7 <= userInput <= 9:
  output = 'sufficient level'

elif 10 <= userInput <= 12:
  output = 'high level'

else:
  output = 'level is absent'

print(output)
