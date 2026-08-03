# Swap two variables

a = input("Enter first value: ")
b = input("Enter second value: ")

print("Before swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping")
print("a =", a)
print("b =", b)

# Temperature conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Area of a circle

import math

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2

print("Area of the circle:", area)