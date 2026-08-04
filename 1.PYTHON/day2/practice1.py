# If Statement

age = 18

if age >= 18:
    print("You are eligible to vote.")

# If-Else Statement

age = 15

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# If-Elif-Else Statement

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested If Statement

number = 10
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")

# Comparison Operators

num = 10

if num == 10:
    print("Number is 10")

# Logical Operators

# AND Operator

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Denied")

# OR Operator

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# NOT Operator

logged_in = False

if not logged_in:
    print("Please log in.")

