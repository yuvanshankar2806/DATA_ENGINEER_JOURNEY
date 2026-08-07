# Prime Number from 1 to 10

i = 1

while i <= 10:
    print(i)
    i += 1

# Print Even from 1 to 100

i = 2

while i <= 20:
    print(i)
    i += 2

# Print Odd from 1 to 100

i = 1

while i <= 20:
    print(i)
    i += 2

# Multiplication Table of 5

num = 7
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# Sum of first 10 natural numbers

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)

# Factorial of a number

num = 5
fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial =", fact)


# Reverse a number

num = 1234

while num > 0:
    digit = num % 10
    print(digit, end="")
    num //= 10

    