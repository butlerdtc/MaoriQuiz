""" V4 of code for getting user details
This version takes code from v2 and places it in an if statement to check if
the age entered by the user is an integer by using the 'is.digit()' method.
This stops the program from crashing when an invalid number is added.
"""

# Asks user for their name to personalize experience
name = input("Please enter your name: ")
# Asks user for age
age = input("Please enter your age: ")

# If statement to check if age is an integer and then run the v2 code
if age.isdigit():
    # Converts age to integer
    age = int(age)
    # If statement so when age is less than 8 it recommends a difficulty of 1
    if 0 < age <= 8:
        difficulty = "1"

    # If age is less than (or equal to) 15 it recommends a difficulty of 2
    elif age <= 15:
        difficulty = "2"

    # If age is anything else it recommends a difficulty of 3
    else:
        difficulty = "3"
else:
    difficulty = "invalid input"

if difficulty != "invalid input":
    print(f"{difficulty}")
else:
    input("Please enter a whole number: ")
