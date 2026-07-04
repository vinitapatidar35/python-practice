import requests
"""
datatypes.py

Covers:
- Numeric types: int, float, complex
- Text type: str (single/double/triple quotes)
- Sequence types: list, tuple, range
- Mapping type: dict
- Set types: set, frozenset
- Boolean type: bool
- NoneType and empty string vs None vs whitespace string
- type() and type conversion (casting)
- Built-in functions/methods vs standard library modules (math, random)
  vs external/third-party packages (requests)
"""

age = 25
negative_num = -150

price = 19.99
gravity = 9.81

coordinate = 3 + 5j

name = "Alice"
greeting = 'Hello, World!'
multiline_string = """This is a string
that spans multiple lines, 
useful for docstrings or paragraphs."""

fruits = ["apple", "banana", "cherry", "apple"]
fruits[1] = "blueberry"

dimensions = (1920, 1080)

countdown = range(5)

user_profile = {
    "username": "coder123",
    "followers": 1420,
    "is_active": True
}
current_user = user_profile["username"]

unique_user_ids = {101, 102, 103, 101, 102}

immutable_set = frozenset([1, 2, 3, 4])

is_python_fun = True
is_overflow_error = False

database_connection = None

print(type(age))
print(type(fruits))

string_number = "100"
converted_int = int(string_number)
float_version = float(age)

data = ""    # empty string (no characters) - different from None
dataa = " "  # string containing a space - different from empty string and None

print("Hello")
length = len([1, 2, 3])
data_type = type(10.5)

text = "python notes"
print(text.upper())
print(text.replace(" ", "_"))

import math
import random

result = math.floor(5.9)
print(result)

lucky_num = random.randint(1, 10)



response = requests.get("https://api.github.com")
print(response.status_code)