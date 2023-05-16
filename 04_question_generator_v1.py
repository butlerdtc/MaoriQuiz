""" V1 of the random question generator """
# This imports random for use in program
import random

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

# This randomly shuffles the order of the list
random.shuffle(questions_1)

# This loop asks the questions from the list and will ask for input and then
# check if the answer is correct. It will ask  each question once.
for i in questions_1:
    answer = input("Please enter the answer to the question {}: ".format(i[0]))
    if answer == i[1]:
        # If answer is correct this prints correct
        print("correct")
    else:
        # If answer is incorrect this prints incorrect
        print("incorrect")
# Test Statement
print("End")
