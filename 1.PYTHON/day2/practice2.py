# EVEN or ODD number check

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# positive or negative number check

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

# Largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")

# Eligibility to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Check the password

password = input("Enter password: ")

if password == "python123":
    print("Login Successful")
else:
    print("Wrong Password")

# Check if a number is divisible by 5

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
    