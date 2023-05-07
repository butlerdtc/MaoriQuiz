""" V2 of code for getting user details
This adds if statements to calculate and recommend them a difficulty level
(will help in later components).
"""

# Asks user for their name to personalize experience
name = input("Please enter your name: ")
# Asks user for age to help in later versions
age = int(input("Please enter your age: "))

# If statement so when age is less than 8 it recommends a difficulty of 1
if 0 < age <= 8:
    difficulty = "1"

# If age is less than (or equal to) 15 it recommends a difficulty of 2
elif age <= 15:
    difficulty = "2"

# If age is anything else it recommends a difficulty of 3
else:
    difficulty = "3"

# Output
print(f"Difficulty = {difficulty}")
