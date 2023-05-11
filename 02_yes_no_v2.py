""" Yes/No checker v2
Asks user for input then simplifies input by converting to lower case.
Also, accepts 'y' or 'n' abbreviations as valid input. Prints result of user
choice and user input - for testing.
Code from Lucky Unicorn 01_yes_no_v2. Reused for efficiency.
"""


# Ask user if they have played before
show_instructions = input("Have you played this quiz before?: ").lower()

# If yes output 'Program continues
if show_instructions == "yes" or show_instructions == "y":
    print("Program continues")

# If no output 'Show instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display Instructions")

# Otherwise show 'Error'
else:
    print("Please enter 'yes' or 'no'")

# Test statement
print(f"You entered '{show_instructions}'")
