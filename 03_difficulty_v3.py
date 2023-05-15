""" V3 of asking for difficulty level
This converts v2 into a function. This function could be reused in any program
after adjustments are made.
"""


# Function to ask user for a difficulty level
def difficulty_levels():
    # Statement to explain differences in difficulty levels
    print()
    print("This is a quiz about numbers in Maori. "
          "This quiz has three different levels of difficulty.\n"
          "Level 1 is the easiest difficulty\n"
          "Level 2 is medium difficulty\n"
          "Level 3 is the hardest difficulty\n"
          "You were recommended a difficulty earlier, but you are free to "
          "choose any level."
          "\n"
          "You can also come back for the other difficulty levels.")
    print()

    # While loop to check if user input is valid/invalid then run accordingly
    while True:
        # Asks for user input
        level = input("Please choose a difficulty, enter 1, 2, or 3: ")
        # Checks if input is valid (1, 2, or 3) then ends the loop
        if level == "1" or level == "2" or level == "3":
            # Prints user input
            print(f"You entered {level}")
            # If level is 1 it will set chosen_level to 1
            if level == "1":
                chosen_level = 1
            # If level is 2 it will set chosen_level to 2
            elif level == "2":
                chosen_level = 2
            # If level is anything else (only possible remaining value is 3) it
            # will set chosen_value to 3
            else:
                chosen_level = 3
            # Prints result of user input
            print(f"You have chosen a difficulty level of {chosen_level}")
            return chosen_level
        # If invalid the loop repeats
        else:
            print("Invalid input, please choose a valid difficulty level")


# Main routine
difficulty_levels()
