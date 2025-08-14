"""
Day 02 - Data Types

Challenge:
Store strings, ints, floats, and booleans; print their types. Ask AI: 'Give me 3 examples of type conversion in Python.'

How to use AI today (examples):
- Ask: Add type hints and a detailed docstring.
- Ask: Write 3 pytest tests with edge cases.
- Ask: Explain time complexity of this solution.
"""

# Start here
def main():
    # TODO: implement today's challenge
    name = "Antony"
    age = 39
    height = 1.75  # in meters
    is_student = False

    print(f"Name: {name} (Type: {type(name)})")
    print(f"Age: {age} (Type: {type(age)})")
    print(f"Height: {height} (Type: {type(height)})")
    print(f"Is Student: {is_student} (Type: {type(is_student)})")

    # Example of type conversion
    age_str = str(age)  # int to str
    height_int = int(height)  # float to int
    is_student_int = int(is_student)  # bool to int

    print(f"Converted Age: {age_str} (Type: {type(age_str)})")
    print(f"Converted Height: {height_int} (Type: {type(height_int)})")
    print(f"Converted Is Student: {is_student_int} (Type: {type(is_student_int)})") 


if __name__ == "__main__":
    main()
