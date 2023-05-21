""" Component 5 - Statement Formatter v2
Function from v2 modified to call function 3 times for testing.
Based off 07_statement_formatter_v3 from Lucky Unicorn for efficiency.
"""


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("!", "Welcome to this Maori Quiz"))
print()
print(formatter("*", "This is a quiz about numbers and days in Maori"))
print()
print(formatter("#", "Thank you for completing this quiz!"))
