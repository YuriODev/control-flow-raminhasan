# Your solution to Exercise 3

userInput = int(input('Input a number from 0 to 36: '))

output = ''
if userInput == 0:
  output = 'green'

elif 1 <= userInput <= 10:
  if userInput % 2 == 1:
    output ='red'

  else:
    output = 'black'

elif 11 <= userInput <= 18:
  if userInput % 2 == 1:
    output ='black'

  else:
    output = 'red'

elif 19 <= userInput <= 28:
  if userInput % 2 == 1:
    output ='red'
  
  else:
    output = 'black'

elif 29 <= userInput <= 36:
  if userInput % 2 == 1:
    output ='black'
  
  else:
    output = 'red'

else:
  print('Invalid')

print(output)
