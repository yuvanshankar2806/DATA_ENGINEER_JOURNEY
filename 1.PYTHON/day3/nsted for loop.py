# Syntax for nested for loops

for i in range(...):
    for j in range(...):
        # code block to be executed for each combination of i and j
        pass    

# EG 1

for i in range(3):
    for j in range(2):
        print(i, j)

# Square pattern using nested for loops

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

# Right-angled triangle pattern using nested for loops

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Number triangle pattern using nested for loops

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Reverse number triangle pattern using nested for loops

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 