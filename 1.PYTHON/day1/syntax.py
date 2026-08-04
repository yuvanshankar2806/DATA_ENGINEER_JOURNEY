# print

print("Hello, World!")
print("Welcome to my Python Learning Journey!")

# Variables

name = "John"
age = 20
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# User Input

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("You are", age, "years old.")

# Data Types

name = "Alice"
age = 22
height = 5.5
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))

# Simple calculations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Age calculation

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("Your age is:", age)