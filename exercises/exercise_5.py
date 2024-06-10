# Your solution to Exercise 5
import math

a = float(input())
b = float(input())
c = float(input())

D = (b ** 2) - 4 * a * c

if a == 0 and b == 0 and c == 0:
  print("Infinite roots.")

elif a == 0 and b == 0 and c != 0:
  print("No roots.")

elif a == 0 and b != 0 and c != 0:
  solution = -1 * c / b
  print(solution)

elif a != 0 and b == 0:
  sol1 = 0
  sol2 = math.sqrt(-1 * c / a)
  print(f'{sol1} and {sol2}')


