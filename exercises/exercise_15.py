# Your solution to Exercise 15

day = int(input())
month = int(input())
year = int(input())

output = ''

leap_year = (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0

if month == 2:
  if leap_year and day == 29:
    day = 1
    month += 1

  elif not leap_year and day == 28:
    day = 1
    month += 1

  elif day > 28 or (leap_year and day > 29):
    day += 1

  else:
    output = 'Invalid date'

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
  if day == 31:
    day = 1
    month += 1

  elif day < 31:
    day += 1

  else: 
    output = 'Invalid date'

elif month == 4 or month ==  6 or month == 9 or month == 11:
  if day == 30:
    day = 1
    month += 1

  elif day < 30:
    day += 1

  else:
    output = 'Invalid date'

elif month == 12:
  if day == 31:
    day = 1
    month = 1
    year += 1

  elif day < 31:
    day += 1

  else:
    output = 'Invalid date'

else:
  output = 'Invalid date'

if output == '':
  print(f'{day}.{month}.{year}')
