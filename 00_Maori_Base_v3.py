""" Maori Quiz Base Component v3
Adds instructions and formats some important text with formatter
Based on 00_Maori_Base_v2
Functions added from component 6
Created by Robson Butler
18/05/23
"""
# This imports random for use in program
import random


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Function to ask for user input and then use that to recommend a difficulty
def get_details():
    # Displays welcome message and uses statement formatter
    print()
    print(formatter("!", "Welcome to this Maori Quiz."))
    print()
    print(" This is a quiz about numbers and the days of the week in Maori.")
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
    print(f"Welcome to the quiz {name}, good-luck! ")
    print(f"We recommended you a difficulty of {difficulty}")
    print()


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


# Function to ask user for a difficulty level
def difficulty_levels():
    # Statement to explain differences in difficulty levels
    print()
    print(formatter("*", "This is a quiz about numbers in Maori. "))
    print("This quiz has three different levels of difficulty.\n"
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
            print(formatter("~", f"You have chosen a difficulty level of "
                                 f"{chosen_level}"))
            print()
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
    # Score variable to calculate their result
    score = 0

    # If statements to run program depending on chosen difficulty level
    if level_chosen == "1":
        # This loop asks the questions from list 1 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_1:
            answer = input("Please answer: {}: "
                           .format(i[0]))
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
                # Adds 1 to score
                score += 1
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
                score += 0
        # Variable to be set to a value of 1 (used in score function)
        challenge = "1"
    elif level_chosen == "2":
        # This loop asks the questions from list 2 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_2:
            answer = input("Please answer: {}: "
                           .format(i[0]))
            # Makes answer capitalization correct
            answer = answer.lower()
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
                # Adds 1 to score
                score += 1
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
                score += 0
        # Variable to be set to a value of 2 (used in score function)
        challenge = "2"
    else:
        # This loop asks the questions from list 3 and will ask for input and
        # then check if the answer is correct. It will ask  each question once.
        for i in questions_3:
            answer = input("Please answer: {}: "
                           .format(i[0]))
            # Makes answer capitalization correct
            answer = answer.title()
            if answer == i[1]:
                # If answer is correct this prints correct
                print("Correct")
                # Adds 1 to score
                score += 1
            else:
                # If answer is incorrect this prints incorrect
                print("Incorrect")
                score += 0
        # Variable to be set to a value of 3 (used in score function)
        challenge = "3"
    # Returns challenge (difficulty) level and user score
    return challenge, score


# Function to calculate user score from question function
def calculate_result(level_, score):
    # Checks if difficulty level chosen is 3, so the result will be out of 7
    if level_ == "3":
        # If score is between 0 and 2 this prints 'Better luck next time'
        if 0 <= score <= 2:
            print()
            print(formatter("^", f"You scored {score}/7"))
            print("Better luck next time")
        # If score is between 3 and 4 this prints 'Not bad'
        elif 2 < score <= 4:
            print()
            print(formatter("^", f"You scored {score}/7"))
            print("Not bad")
        # If score is between 5 and 6 this prints 'Good job'
        elif 4 < score <= 6:
            print()
            print(formatter("^", f"You scored {score}/7"))
            print("Good job")
        # If score is 7 it prints perfect score and congratulates user
        else:
            print()
            print(formatter("^", f"You scored {score}/7"))
            print("You got a perfect score! Congratulations")
    # If difficulty is anything else (1 or 2) the result will be out of 10
    else:
        # If score is between 0 and 3 this prints 'Better luck next time'
        if 0 <= score <= 3:
            print()
            print(f"You scored {score}/10\n"
                  f"Better luck next time")
        # If score is between 4 and 6 this prints 'Not bad'
        elif 3 < score <= 6:
            print()
            print(f"You scored {score}/10\n"
                  f"Not bad")
        # If score is between 7 and 9 this prints 'Good job'
        elif 6 < score <= 9:
            print()
            print(f"You scored {score}/10\n"
                  f"Good job")
        # If score is 10 it prints perfect score and congratulates the user
        else:
            print()
            print(f"You scored {score}/10\n"
                  f"You got a perfect score! Congratulations")
    # Prints a thank-you message after printing the score
    print()
    print(formatter("*", "Thank you for completing this quiz!"))


# Main routine
get_details()
# Code to call yes/no function
played = yes_no("Have you played the quiz before? ")

# Instructions if they input no when asked if they have played before
if played == "No":
    print("This is a quiz about numbers and days in Maori\n"
          "Please choose a difficulty level to decide which questions you will"
          "be asked\n"
          "Then answer the question with correct spelling and after all are "
          "answered it will show you your score")

# Code to call difficulty_levels() and question_generator()
difficulty_level, result = question_generator()
# Calls function and uses difficulty level and result from previous function
calculate_result(difficulty_level, result)
