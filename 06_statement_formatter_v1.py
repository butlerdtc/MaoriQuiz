""" Component 5 - Statement Formatter v1
Component from 07_statement_formatter_v1 from Lucky Unicorn.
It serves the same purpose as it did in Lucky Unicorn, so I reused the code
"""

# Variables to be formatted
symbol = "-"
text = "Welcome to this quiz about Maori numbers and days of the week"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = "-" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
