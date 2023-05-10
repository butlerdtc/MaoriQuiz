""" V5 of code for getting user details
This version takes code from v3 and turns it into a function
"""


# Function to ask for user input and then use that to recommend a difficulty
def get_details():
    # Asks user for their name to personalize experience
    name = input("Please enter your name: ")
    age = ""

    while age == "":
        if age == "":
            while not age:
                try:
                    age = int(input("Please enter your age: "))
                except ValueError:
                    age = int(input("Please enter a whole number: "))

            # If statement so when age is less than 8 it recommends a
            # difficulty of 1
            if 0 < age <= 8:
                difficulty = "1"

            # If age is less than (or equal to) 15 it recommends a difficulty
            # of 2
            elif age <= 15:
                difficulty = "2"

            # If age is anything else it recommends a difficulty of 3
            else:
                difficulty = "3"

            # Output
            print(f"Name = {name}")
            print(f"Age = {age}")
            print(f"Recommended difficulty = {difficulty}")

        else:
            age = int(input("Please enter a whole number: "))
            # If statement so when age is less than 8 it recommends a
            # difficulty of 1
            if 0 < age <= 8:
                difficulty = "1"

            # If age is less than (or equal to) 15 it recommends a difficulty
            # of 2
            elif age <= 15:
                difficulty = "2"

            # If age is anything else it recommends a difficulty of 3
            else:
                difficulty = "3"

            # Output
            print(f"Name = {name}")
            print(f"Age = {age}")
            print(f"Recommended difficulty = {difficulty}")


# Main routine
get_details()
