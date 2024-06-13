# Your solution to Exercise 6

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

output = "No roots."

if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."

elif a == 0:
    if b != 0:
        output = f"{-c / b}"

elif b == 0:
    if c != 0:
        #  -(-c / a) ** 0.5
        x1 = (-c / a) ** 0.5
        x2 = -(-c / a) ** 0.5
        output = f"{x1} and {x2}"
    else:
        # If coefficient c is 0, set the output to "0"
        output = "0"

# If neither coefficient a nor b is 0, calculate the discriminant d
else:
    d = b ** 2 - 4 * a * c

    # Check if the discriminant d is greater than 0
    if d > 0:
        # If d is greater than 0, calculate the roots using
        # the quadratic formula
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        output = f"{x1} and {x2}"

    # Check if the discriminant d is equal to 0
    elif d == 0:
        # If d is equal to 0, calculate the root using the formula -b / (2 * a)
        x = -b / (2 * a)
        output = f"{x}"

# Print the output
print(output)
