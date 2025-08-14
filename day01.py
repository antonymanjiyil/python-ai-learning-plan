"""
Day 01 - Printing & Variables

Challenge:
Print your name, age, and today's date. Ask AI: 'Format this output nicely using f-strings.'

How to use AI today (examples):
- Ask: Refactor this function to be more Pythonic.
- Ask: Add type hints and a detailed docstring.
- Ask: Write 3 pytest tests with edge cases.
"""
from datetime import date
# Start here
def main():
    # TODO: implement today's challenge
    name = "Antony"
    age = 39
    today = date.today().strftime("%d-%m-%Y")   
    print(f"Name: {name}\nAge: {age}\nToday's Date: {today}")



if __name__ == "__main__":
    main()
