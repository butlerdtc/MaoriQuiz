""" V3 of code for getting user details
This adds if statements to calculate and recommend them a difficulty level
(will help in later components).
"""

# Asks user for their name to personalize experience
name = input("Please enter your name: ")
# Asks user for age to help in later versions
age = int(input("Please enter your age: "))

# Variables to use instead of literals
minimum = 0
level_1 = 8
level_2 = 15
level_3 = 120

while minimum <= age:
    # If statement so when age is less than 8 it recommends a difficulty of 1
    if minimum < age <= level_1:
        difficulty = "1"
        # Output
        print(f"Recommended difficulty = {difficulty}")

    # If age is less than (or equal to) 15 it recommends a difficulty of 2
    elif age <= level_2:
        difficulty = "2"
        # Output
        print(f"Recommended difficulty = {difficulty}")

    # If age is anything else it recommends a difficulty of 3
    elif age <= level_3:
        difficulty = "3"
        # Output
        print(f"Recommended difficulty = {difficulty}")

    else:
        int(input("Please enter your age (as a whole number): "))
