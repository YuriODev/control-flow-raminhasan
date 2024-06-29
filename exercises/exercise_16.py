# Your solution to Exercise 16

day = int(input())
month = int(input())
year = int(input())

output = ''

leap_year = (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0

if month == 3:
  if leap_year:
    day = 29
    month -= 1

  elif 1 < day  <= 31:
    day -= 1

  else:
    output = 'Invalid date'

elif month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
  if day == 3:
    day = 31
    month -= 1

  elif 1 < day < 31:
    day -= 1

  else:
    output = 'Invalid date'

elif month == 5 or month == 7 or month == 10 or month == 12:
  if day == 1:
    day = 30
    month -= 1

  elif 1 < day < 31:
    day -= 1

  else:
    output = 'Invalid date'

elif month == 1:
  if day == 1:
    day = 31
    month = 12
    year -= 1

  elif 1 < day < 31:
    day -= 1

  else:
    output = 'Invalid date'

else: 
  output = 'Invalid date'

if output == '':
  print(f"{day}.{month}.{year}")
