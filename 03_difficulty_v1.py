""" V1 of asking for difficulty level """

# Statement to explain differences in difficulty levels
print()
print("This is a quiz about numbers in Maori. "
      "This quiz has three different levels of difficulty.\n"
      "Level 1 is the easiest difficulty\n"
      "Level 2 is medium difficulty\n"
      "Level 3 is the hardest difficulty\n"
      "You were recommended a difficulty but you are free to choose any level."
      "\n"
      "You can also come back for the other difficulty levels.")
print()
# Variable to ask for user input for their choice of level
level = int(input("Please enter either 1, 2, or 3 to choose a level: "))

# If statement to calculate and print level depending on their input
if level == 1 or 2 or 3:
    if level == 1:
        print("Level 1")
    elif level == 2:
        print("Level 2")
    elif level == 3:
        print("Level 3")
    # Else statement to print an error message for invalid input
    else:
        print("Please enter 1, 2, or 3")
# Else statement to ask for level if user input was invalid (not an integer)
else:
    int(input("Please enter 1, 2, or 3: "))
