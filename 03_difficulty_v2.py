""" V2 of asking for difficulty level
This is based off of version 1. It uses a while true loop to ask and check if
the input entered is valid (1, 2, or 3) and if invalid it will ask again. If
input is valid it will print the respective level (needed in next component).
"""

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

# While loop to check if user input is valid/invalid then run accordingly
while True:
    # Asks for user input
    level = input("Please choose a difficulty, enter 1, 2, or 3: ")
    # Checks if input is valid (1, 2, or 3) then ends the loop
    if level == "1" or level == "2" or level == "3":
        print(f"You entered {level}")
        break
    # If invalid the loop repeats
    else:
        print("Invalid input, please choose a valid difficulty level")

# If level is 1 it will print 'Level 1'
if level == "1":
    print()
    print("Level 1")
# If level is 2 it will print 'Level 2'
elif level == "2":
    print()
    print("Level 2")
# If level is anything else (only possible remaining value is 3) it will print
# 'Level 3'
else:
    print()
    print("Level 3")
