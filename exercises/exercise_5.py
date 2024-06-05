# Your solution to Exercise 5
import math

a = int(input())
b = int(input())
c = int(input())

root1 = ''
root2 = ''

try:
  sol1 = (-1 * b + math.sqrt((b^2) - 4 * a * c) / 2 * a )
  root1 = sol1

except ValueError:
  root1 = False

try:
  sol2 = (-1 * b - math.sqrt((b^2) - 4 * a * c) / 2 * a )
  root2 = sol2

except ValueError:
  root2 = False

if root1 != False and root2 != False:
  print(f'{root1} and {root2}')

elif root1 == root2 != False:
  print(f'{root1}')

elif not root1 and not root2:
  print('No roots.')

else:
  print('Infinite roots.')
