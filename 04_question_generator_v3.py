""" V2 of the random question generator
This version adds to v1. This uses the function from 03_difficulty_v3 to ask
for a difficulty level which will be used to choose which list to run in the
program. This also adds the question sets for difficulty levels 2 and 3.
"""
# This imports random for use in program
import random


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
                chosen_level = "1"
            # If level is 2 it will set chosen_level to 2
            elif level == "2":
                chosen_level = "2"
            # If level is anything else (only possible remaining value is 3) it
            # will set chosen_value to 3
            else:
                chosen_level = "3"
            # Prints result of user input
            print(f"You have chosen a difficulty level of {chosen_level}")
            return chosen_level
        # If invalid the loop repeats
        else:
            print("Invalid input, please choose a valid difficulty level")


# Function to ask question and check answer
def question_generator():
    # The set of questions for difficulty level 1
    questions_1 = [["What is tahi in english? ", "1"],
                   ["What is rua in english? ", "2"],
                   ["What is toru in english? ", "3"],
                   ["What is wha in english? ", "4"],
                   ["What is rima in english? ", "5"],
                   ["What is ono in english? ", "6"],
                   ["What is whitu in english? ", "7"],
                   ["What is waru in english? ", "8"],
                   ["What is iwa in english? ", "9"],
                   ["What is tekau in english? ", "10"]]

    # The set of questions for difficulty level 2
    questions_2 = [["What is 1 in Maori? ", "tahi"],
                   ["What is 2 in Maori? ", "rua"],
                   ["What is 3 in Maori? ", "toru"],
                   ["What is 4 in Maori? ", "wha"],
                   ["What is 5 in Maori? ", "rima"],
                   ["What is 6 in Maori? ", "ono"],
                   ["What is 7 in Maori? ", "whitu"],
                   ["What is 8 in Maori? ", "waru"],
                   ["What is 9 in Maori? ", "iwa"],
                   ["What is 10 in Maori? ", "tekau"]]

    # The set of questions for difficulty level 3
    questions_3 = [["What is Rahina in english? ", "Monday"],
                   ["What is Ratu in english? ", "Tuesday"],
                   ["What is Raapa in english? ", "Wednesday"],
                   ["What is Rapare in english? ", "Thursday"],
                   ["What is Ramere in english? ", "Friday"],
                   ["What is Rahoroi in english? ", "Saturday"],
                   ["What is Ratapu in english? ", "Sunday"]]

    # This randomly shuffles the order of the list
    random.shuffle(questions_1)
    random.shuffle(questions_2)
    random.shuffle(questions_3)

    # Variable to be assigned value from difficulty_levels function
    level_chosen = difficulty_levels()

    # If statements to run program depending on chosen difficulty level
    if level_chosen == "1":
        # This loop asks the questions from list 1 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_1:
            answer = input("Please enter the answer to the question {}: "
                           .format(i[0]).lower())
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
    elif level_chosen == "2":
        # This loop asks the questions from list 2 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_2:
            answer = input("Please enter the answer to the question {}: "
                           .format(i[0]).lower())
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
    else:
        # This loop asks the questions from list 3 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_3:
            answer = input("Please enter the answer to the question {}: "
                           .format(i[0]).lower())
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
    # Test Statement
    print("End")


# Main routine
question_generator()
