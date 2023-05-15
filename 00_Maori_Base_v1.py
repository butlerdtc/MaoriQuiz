""" Maori Quiz Base Component v1
Each component gets added after creation and testing.
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

    # A loop to ask for their age and check if input is a valid integer
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


# Function to ask if they have played and check for valid input of yes or no
def yes_no(question_text):
    while True:

        # Ask user if they have played before
        answer = input(question_text).lower()

        # If yes output 'Program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no output 'Show instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise show 'Error'
        else:
            print("Please enter 'yes' or 'no'")


# Main routine
get_details()
# Code to call component 2
show_instructions = yes_no("Have you played the quiz before? ")
print(f"You entered '{show_instructions}'")
