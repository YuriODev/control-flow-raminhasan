# Your solution to Exercise 14

num = input()
first_char = len(num)

if num[-1:-first_char] == num:
  print("True")

else:
  print("False")
