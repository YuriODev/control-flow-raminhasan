# Your solution to Exercise 3

userInput = int(input('Input a number from 0 to 36: '))

output = ''
if userInput == 0:
  output = 'Green'

elif 1 <= userInput <= 10:
  if userInput % 2 == 1:
    output ='Red'

  else:
    output = 'Black'

elif 11 <= userInput <= 18:
  if userInput % 2 == 1:
    output ='Black'

  else:
    output = 'Red'

elif 19 <= userInput <= 28:
  if userInput % 2 == 1:
    output ='Red'
  
  else:
    output = 'Black'

elif 29 <= userInput <= 36:
  if userInput % 2 == 1:
    output ='Black'
  
  else:
    output = 'Red'

else:
  print('The bet will not play!')

print(output)
