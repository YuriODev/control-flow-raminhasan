# Your solution to Exercise 15

day = int(input())
month = int(input())
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  if month == 2:
    if day >= 29:
      day = 1
      month += 1

    else:
      day += 1

  elif month == 1 or 3 or 5 or 7 or 8 or 10:
    if day >= 31:
      day = 1
      month += 1

    else:
      day += 1
  elif month == 4 or 6 or 9 or 11:
    if day >= 30:
      day = 1
      month += 1

    else:
      day += 1

  elif month == 12:
    if day >= 31:
      day = 1
      month = 1
      year += 1

    elif:
      day += 1

else:
  if month == 2:
    if day >= 28:
      day = 1
      month += 1

    else:
      day += 1

  elif month == 1 or 3 or 5 or 7 or 8 or 10:
    if day >= 31:
      day = 1
      month += 1

    else:
      day += 1
  elif month == 4 or 6 or 9 or 11:
    if day >= 30:
      day = 1
      month += 1

    else:
      day += 1

  elif month == 12:
    if day >= 31:
      day = 1
      month = 1
      year += 1

    elif:
      day += 1
