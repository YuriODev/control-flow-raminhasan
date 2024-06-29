# Your solution to Exercise 17

ticket_num = int(input())

ones = ticket_num % 10
tens = (ticket_num % 100) // 10
huns = (ticket_num % 1000) // 100

last_digit_sum = ones + tens + huns

hths = ticket_num // 100000
tths = (ticket_num % 100000) // 10000
thos = ((ticket_num % 100000) % 10000) // 1000

first_digits_sum = hths + tths+ thos

if first_digits_sum == last_digit_sum:
  print("Happy")

else:
  print("Ordinary")
