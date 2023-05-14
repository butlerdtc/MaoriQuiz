""" Maori Quiz Yes/No Checker v4
Converts v3 code into a function. Fixes the problem from v1 and v2, so it is
now looped correctly and will continue to ask until valid input is entered.
Code from Lucky Unicorn 02_yes_no_function_v1. Reused.
"""


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
show_instructions = yes_no("Have you played the quiz before? ")
print(f"You entered '{show_instructions}'")
