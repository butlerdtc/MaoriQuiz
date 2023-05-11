""" V3 of code for getting user details
This version takes code from v2 and places it in an if statement to check if
the age entered by the user is an integer by using a try and accept loop.
This stops the program from crashing when an invalid number is added.
"""

# Asks user for their name to personalize experience
name = input("Please enter your name: ")
age = ""

# While loop to run loop to ask for correct input for their age
while age == "":
    if age == "":
        # Integer checker
        while not age:
            try:
                age = int(input("Please enter your age: "))
            except ValueError:
                age = int(input("Please enter a whole number: "))

        # If statement so when age is less than 8 it recommends a difficulty
        # of 1
        if 0 < age <= 8:
            difficulty = "1"

        # If age is less than (or equal to) 15 it recommends a difficulty of 2
        elif age <= 15:
            difficulty = "2"

        # If age is anything else it recommends a difficulty of 3
        else:
            difficulty = "3"

        # Output
        print(f"Recommended difficulty = {difficulty}")
    else:
        age = int(input("Please enter a whole number: "))
        # If statement so when age is less than 8 it recommends a difficulty
        # of 1
        if 0 < age <= 8:
            difficulty = "1"

        # If age is less than (or equal to) 15 it recommends a difficulty of 2
        elif age <= 15:
            difficulty = "2"

        # If age is anything else it recommends a difficulty of 3
        else:
            difficulty = "3"

        # Output
        print(f"Recommended difficulty = {difficulty}")
