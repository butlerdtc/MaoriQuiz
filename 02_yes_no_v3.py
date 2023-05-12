""" Maori Quiz Yes/No Checker v3
Uses code from v2 and places it into a loop to make testing more efficient.
Code from Lucky Unicorn 01_yes_no_v3. Reused to be efficient.
"""


# Loop for code to make testing efficient
show_instructions = ""
while show_instructions != "1":
    # Ask user if they have played before
    show_instructions = input("Have you played the quiz before?: ").lower()

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
