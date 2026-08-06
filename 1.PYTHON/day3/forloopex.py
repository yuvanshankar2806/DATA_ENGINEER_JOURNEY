# print numbers from 0 to 4

for i in range(5):
    print(i)

# start and end values

for i in range(2, 6):
    print(i)

# start, end, and step values

for i in range(2, 11, 2):
    print(i)

# reapting a string multiple times

for i in range(5):
    print("Yuvan")

# Sum of numbers from 1 to 6                               

total = 0

for i in range(1, 6):
    total = total + i

print("Sum =", total)

# Multiplication table of 5

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# factorial of a number

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)