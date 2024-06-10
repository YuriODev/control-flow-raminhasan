# Your solution to Exercise 5
import math

a = float(input())
b = float(input())
c = float(input())

D = (b ** 2) - 4 * a * c

if a == 0:
    if b == 0 and c == 0:
      print("Infinite roots.")

    elif b == 0 and c != 0:
      print("No roots.")

    elif b != 0:
      solution = -1 * c / b
      print(solution)

elif a != 0 and b == 0:
  sol1 = 0
  sol2 = math.sqrt(-1 * c / a)
  print(f'{sol1} and {sol2}')

elif c == 0:
  sol1 = 0
  sol2 = (-1 * b) / a
  print(f'{sol1} and {sol2}')

elif D != 0:
  sol1 = ((-1 * b) + math.sqrt(D)) / (2 * a)
  sol2 = ((-1 * b) - math.sqrt(D)) / (2 * a)
  print(f'{sol1} and {sol2}')

elif D == 0:
  sol = (-1 * b) / (2 * a)
  print(sol)
