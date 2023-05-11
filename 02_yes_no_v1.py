""" V1 of code for Yes/No Checker
Code from Lucky Unicorn 01_yes_no_v1. Same purpose so I reused the base code.
"""


# Ask user if they have played the quiz before
show_instructions = input("Have you played this quiz before?: ")

# If yes output 'Program continues'
if show_instructions == "yes":
    print("Program continues")

# If no output 'Show instructions'
elif show_instructions == "no":
    print("Display Instructions")

# Otherwise show 'Error'
else:
    print("Please enter 'yes' or 'no'")
