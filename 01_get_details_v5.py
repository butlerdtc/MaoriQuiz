""" V5 of code for getting user details
This version takes code from v3 and turns it into a function. Changes were made
so that if invalid input is entered when the question repeats, it prints an
error message, it will not crash and the loop will continue until valid input
is entered. Also displays a welcome message now.
"""


# Function to ask for user input and then use that to recommend a difficulty
def get_details():
    # Displays welcome message and empty print statements for aesthetics
    print()
    print("Welcome to this Maori Quiz. This is a quiz about numbers in Maori.")
    print()
    # Asks user for their name to personalize experience
    name = input("Please enter your name: ")
    age = ""
    # Variables made to replace literals
    level_1 = 1
    level_2 = 2
    level_3 = 3
    middle_bracket = 15
    lower_bracket = 8

    # A loop to check if user input is a valid integer
    while not age:
        error = "Age must be a whole number"
        try:
            age = int(input("Please enter your age: "))
        except ValueError:
            print(error)

    # If statement so when age is less than 8 it recommends a difficulty of 1
    if 0 < age <= lower_bracket:
        difficulty = level_1

    # If age is less than (or equal to) 15 it recommends a difficulty of 2
    elif age <= middle_bracket:
        difficulty = level_2

    # If age is anything else it recommends a difficulty of 3
    else:
        difficulty = level_3

    # Output
    print(f"Name = {name} ")
    print(f"Age = {age}")
    print(f"Recommended difficulty = {difficulty}")


# Main routine
get_details()
