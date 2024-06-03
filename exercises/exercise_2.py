# Your solution to Exercise 2

userAge = int(input('How old are you? '))

output = ''
if userAge <= 1:
  output = 'You are an infant.'

elif 1 < userAge < 13:
  output = 'You are a child.'

elif 13 <= userAge < 20:
  output = 'You are a teenager.'

else: 
  output = 'You are an adult.'

print(output)
