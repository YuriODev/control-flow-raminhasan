# Your solution to Exercise 6

A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

distA = ((A2 ** 2) + (A1 ** 2)) ** (1/2)  
distB = ((B2 ** 2) + (B1 ** 2)) ** (1/2)

if distA == distB:
  print("A and B are at the same distance from the origin.")

elif distA < distB:
  print("B is further from the origin.")

elif distA > distB:
  print("A is further from the origin.")
