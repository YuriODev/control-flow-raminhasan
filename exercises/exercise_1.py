# Your solution to Exercise 1

ageAlex = int(input('How old is Alex? '))
ageTatyana = int(input('How old is Tatyana? '))

output = ''
if ageAlex > ageTatyana:
  output = 'Alex is the eldest.'

elif ageTatyana > ageAlex:
  output = 'Tatyana is the eldest.'

else:
  output = 'Alex and Tatyana are of the same age.'

print(output)