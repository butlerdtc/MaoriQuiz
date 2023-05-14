""" V3 of asking for difficulty level """


# Variable to ask for user input for their choice of level
final_level = ""
level = ""

while level == "":
    error = "Please enter either 1, 2, or 3"
    try:
        level = int(input("Please enter either '1', '2', or '3' to choose a "
                          "level: "))
    except ValueError:
        print(error)

# If statement to calculate and print level depending on their input
if level == 1:
    print("Level 1")
elif level == 2:
    print("Level 2")
elif level == 3:
    print("Level 3")
