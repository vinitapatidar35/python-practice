# ==============================================================================
# PYTHON DATA TYPES REFERENCE SHEET (VS Code Notes)
# ==============================================================================
# In Python, variables are dynamically typed. 
# You don't need to declare a type; Python infers it at runtime.
# Use the type() function to check a variable's data type.

# ------------------------------------------------------------------------------
# 1. NUMERIC TYPES
# ------------------------------------------------------------------------------

# int: Integer values (whole numbers, positive or negative)
age = 25
negative_num = -150

# float: Floating-point numbers (numbers with a decimal point)
price = 19.99
gravity = 9.81

# complex: Complex numbers (written with a 'j' or 'J' as the imaginary part)
coordinate = 3 + 5j


# ------------------------------------------------------------------------------
# 2. TEXT TYPE
# ------------------------------------------------------------------------------

# str: String values (text wrapped in single, double, or triple quotes)
name = "Alice"
greeting = 'Hello, World!'
multiline_string = """This is a string
that spans multiple lines, 
useful for docstrings or paragraphs."""


# ------------------------------------------------------------------------------
# 3. SEQUENCE TYPES
# ------------------------------------------------------------------------------

# list: Ordered, MUTABLE collection. Allows duplicate items.
# Best used for collections of items that might change.
fruits = ["apple", "banana", "cherry", "apple"]
fruits[1] = "blueberry"  # Allowed because lists are mutable

# tuple: Ordered, IMMUTABLE collection. Allows duplicate items.
# Faster than lists; protects data from being accidentally changed.
dimensions = (1920, 1080)
# dimensions[0] = 1280  # TypeError: tuples cannot be modified after creation

# range: Represents an immutable sequence of numbers.
# Commonly used for looping a specific number of times in 'for' loops.
countdown = range(5)  # Generates numbers from 0 to 4


# ------------------------------------------------------------------------------
# 4. MAPPING TYPE
# ------------------------------------------------------------------------------

# dict: Dictionary. Stores data in key-value pairs.
# Keys must be unique and immutable; values can be anything.
user_profile = {
    "username": "coder123",
    "followers": 1420,
    "is_active": True
}
# Access values using their keys:
current_user = user_profile["username"]


# ------------------------------------------------------------------------------
# 5. SET TYPES
# ------------------------------------------------------------------------------

# set: Unordered, MUTABLE collection of UNIQUE items.
# Automatically removes any duplicates you pass into it. No indexing.
unique_user_ids = {101, 102, 103, 101, 102}  # Evaluates to {101, 102, 103}

# frozenset: Unordered collection of UNIQUE items that is IMMUTABLE.
immutable_set = frozenset([1, 2, 3, 4])


# ------------------------------------------------------------------------------
# 6. BOOLEAN TYPE
# ------------------------------------------------------------------------------

# bool: Boolean values representing truth states.
# Must be capitalized: True or False.
is_python_fun = True
is_overflow_error = False


# ------------------------------------------------------------------------------
# 7. NONE TYPE
# ------------------------------------------------------------------------------

# NoneType: Represents the intentional absence of a value.
# Often used as default values for function arguments or empty states.
database_connection = None


# ==============================================================================
# QUICK TYPE CHECKING AND CONVERSION (EXAMPLES)
# ==============================================================================

# Checking data types:
print(type(age))        # Output: <class 'int'>
print(type(fruits))     # Output: <class 'list'>

# Type Conversion (Casting):
string_number = "100"
converted_int = int(string_number)  # Converts string "100" to integer 100
float_version = float(age)          # Converts integer 25 to float 25.0

data =""# blank and  diff from None, a string value with no char inside
dataa = " " # diff from None its an empty string, string value with 1 or more spaces 



# ==============================================================================
# PYTHON MODULES: QUICK REFERENCE NOTES
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. BUILT-INS (No Import Needed)
# ------------------------------------------------------------------------------
# - Automatically loaded into memory when Python runs.
# - You NEVER use the "import" keyword for these.

# A. Global Functions: Wrap around your data
print("Hello")                  # Outputs text to terminal
length = len([1, 2, 3])         # Counts elements (Output: 3)
data_type = type(10.5)          # Identifies data type (Output: <class 'float'>)

# B. Core Classes (Data Types): Methods attach directly via a dot (.)
text = "python notes"
print(text.upper())             # Output: "PYTHON NOTES"
print(text.replace(" ", "_"))   # Output: "python_notes"


# ------------------------------------------------------------------------------
# 2. STANDARD MODULES (Requires 'import')
# ------------------------------------------------------------------------------
# - Pre-installed with Python (no internet download required).
# - Kept unloaded to save computer RAM until you explicitly ask for them.

import math                     # 1. Bring the module into memory
import random

result = math.floor(5.9)        # 2. Access features using module_name.function()
print(result)                   # Output: 5

lucky_num = random.randint(1, 10) # Generates random number between 1 and 10


# ------------------------------------------------------------------------------
# 3. EXTERNAL MODULES (Requires Installation + Import)
# ------------------------------------------------------------------------------
# - Third-party packages built by the community. Not pre-installed.
# - Must be downloaded from the internet using your terminal first.

# STEP 1: Run this installation command in your VS Code terminal:
# pip install requests

# STEP 2: Import and use it inside your script:
import requests                 # Bring the installed package into memory

response = requests.get("https://api.github.com")
print(response.status_code)     # Output: 200 (Success)
