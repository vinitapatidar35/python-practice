# ==============================================================================
# PYTHON LEARN — MASTER THEORY NOTES
# ==============================================================================
# This file contains ONLY theory — no runnable code exercises.
# Topics are arranged in the order they should be learned, so each new
# topic builds on the one before it. Written so a complete beginner can
# read top to bottom and understand Python from zero.
# ==============================================================================


# ==============================================================================
# 1. INTRODUCTION: print(), COMMENTS, AND HOW PYTHON READS YOUR CODE
# ==============================================================================

# WHAT IS A PROGRAM?
# A program is just a set of instructions given to the computer, written in a
# language it understands. Python is one such language — it is popular because
# its instructions read almost like plain English.

# WHAT IS print()?
# print() is a BUILT-IN FUNCTION. A function is a reusable block of code that
# performs one task when you "call" it. print()'s job is to display whatever
# you give it on the screen (this is called "output" or "console output").
# Syntax: print("whatever you want to show")

# WHAT IS A STRING?
# Any text wrapped in quotes is called a "string" in Python — it is one of
# Python's basic data types, used to store and work with text.
# Both single quotes ('like this') and double quotes ("like this") work
# exactly the same way for normal strings. Pick one style and stay consistent.
# Double quotes are handy when your text itself contains a single quote
# (e.g. "it's raining"), and vice versa.

# WHAT IS A COMMENT?
# A comment is a line that Python completely IGNORES while running the
# program. It exists purely for humans to read — to explain what a piece of
# code does, or to leave a note for your future self or teammates.
# In Python, a comment starts with the # symbol. Everything after # on that
# line is ignored.
#
# IMPORTANT: Python does NOT have an official multi-line comment symbol.
# You can only write single-line comments using #. If people want to
# "comment out" many lines, they either:
#   a) put # in front of every single line, OR
#   b) use a triple-quoted string ( ''' ... ''' or """ ... """ ) sitting
#      somewhere it does nothing logically. Technically this creates a
#      STRING object (not a real comment), but since Python discards it if
#      it's not used or assigned, people use it visually like a block
#      comment. This is also the same syntax used for "docstrings"
#      (see Section 12).

# TYPES OF FUNCTIONS (a preview — explained more in Section 12)
# 1) BUILT-IN FUNCTION — already provided by Python, ready to use immediately,
#    no installation or import needed. Examples: print(), len(), type(), input()
# 2) THIRD-PARTY / EXTERNAL LIBRARY FUNCTION — written by other
#    people/companies, not part of core Python. Must first be INSTALLED
#    (commonly with a tool called "pip") and then IMPORTED into your code
#    before you can use it. Examples: pandas.read_csv(), requests.get()
# 3) USER-DEFINED FUNCTION — created by you, the programmer, using the
#    'def' keyword, to perform a task your specific program needs.

# ESCAPE SEQUENCES
# An escape sequence is a special 2-character code INSIDE a string that
# starts with a backslash (\). It lets you insert characters that are hard
# to type directly, or control how text is laid out when printed. They are
# needed because quotes and the backslash already have special meaning in
# Python strings, so to display them as normal characters you must "escape"
# them.
#
# Common escape sequences:
#   \n   -> New line (moves the rest of the text to the next line)
#   \t   -> Tab space (adds a bigger horizontal gap, like pressing the Tab key)
#   \\   -> One literal backslash character (\)
#   \'   -> A literal single quote character (')
#   \"   -> A literal double quote character (")
#   \b   -> Backspace (deletes/moves back one character in the display)
#
# A single print() call can contain multiple \n characters, letting one
# print() display several lines of text at once.

# TRIPLE-QUOTED STRINGS (MULTI-LINE STRINGS)
# Triple quotes (''' ''' or """ """) let you write a string that spans
# multiple lines directly, exactly as typed, without needing \n everywhere.
# They are also used to write "docstrings" — descriptive text placed as the
# very first statement inside a function, class, or file to document what
# it does. Python officially recognizes a docstring in that position and
# tools like help() can display it automatically.

# EXTRA GOOD-TO-KNOW INFO
# - print() can take multiple items separated by commas:
#     print("Name:", "Vinita") -> automatically inserts a space between them.
# - print() has extra optional settings:
#     end="" -> stops print() from automatically adding a new line at the end
#     sep="-" -> changes the separator placed between comma-separated items
#                (default separator is a single space)


# ==============================================================================
# 2. VARIABLES
# ==============================================================================

# WHAT IS A VARIABLE?
# A variable is a name used to store data in memory so it can be used and
# modified later in a program. Think of it as a labeled container/box: you
# put a value inside, and you can access or change that value later just by
# using its label (name).
# Syntax: variable_name = value
#
# HOW IT WORKS INTERNALLY: when you write name = "Vinita", Python creates
# the string "Vinita" somewhere in memory, and links the label "name" to
# point to it. Whenever you use "name" afterward, Python fetches the value
# it currently points to.

# VARIABLE NAMING RULES
# Valid names:
#   - can contain letters, numbers, and underscores (_)
#   - cannot start with a number
#   - cannot contain hyphens (-) or spaces
#   - cannot be a Python reserved keyword (like "class", "if", "for")
#   - are case-sensitive (age and Age are two different variables)

# MULTIPLE ASSIGNMENT
# Python lets you assign several variables in one line:
#   name, age, city = "Vinita", 21, "Indore"   -> assigns one value to each
#   x = y = z = 0                              -> assigns the SAME value to all

# REASSIGNMENT & DYNAMIC TYPING
# A variable can be given a new value anytime — even a value of a completely
# different data type. This is called DYNAMIC TYPING: Python does not lock a
# variable to one type forever; the type is simply whatever the variable
# currently holds.
#   x = 10        -> x is int
#   x = "hello"   -> x is now str
#   x = 3.14      -> x is now float
# This is different from some other languages where a variable's type must
# be declared once and cannot change.


# ==============================================================================
# 3. DATA TYPES
# ==============================================================================

# Python automatically figures out (infers) a variable's data type based on
# how the value is written — you never have to declare the type yourself.
# Use the built-in type() function to check any variable's current type:
#   type(variable_name) -> returns the data type class

# 1. NUMERIC TYPES
#    - int: whole numbers, positive or negative (e.g. 21, -150)
#    - float: numbers with a decimal point (e.g. 7.07, -4.75)
#    - complex: numbers with a real part and an imaginary part, written with
#      a trailing j or J (e.g. 3 + 5j). Used mainly in scientific/engineering
#      contexts (electrical signals, advanced math).

# 2. TEXT TYPE
#    - str: text wrapped in single, double, or triple quotes.

# 3. SEQUENCE TYPES (ordered collections, accessed by position)
#    - list: ordered, MUTABLE (changeable after creation), allows duplicates.
#      Written with square brackets: [1, 2, 3]
#    - tuple: ordered, IMMUTABLE (cannot be changed after creation), allows
#      duplicates. Written with round brackets: (1, 2, 3). Because it can
#      never change, Python can handle tuples slightly faster than lists,
#      and they are useful when you want to guarantee data won't accidentally
#      be modified.
#    - range: an efficient, immutable sequence of numbers, most commonly
#      used to control how many times a loop repeats.

# 4. MAPPING TYPE
#    - dict (dictionary): stores data as KEY-VALUE pairs, written with curly
#      braces: {"key": "value"}. Keys must be unique and of an immutable
#      type (like a string or number); values can be anything, including
#      duplicates.

# 5. SET TYPES (unordered collections of unique items)
#    - set: unordered, MUTABLE, automatically removes duplicate values,
#      cannot be indexed (no fixed position/order to point to). Written
#      with curly braces without key:value pairs: {1, 2, 3}
#    - frozenset: like a set, but IMMUTABLE once created.

# 6. BOOLEAN TYPE
#    - bool: only two possible values, True or False (always capitalized).
#      Used to represent yes/no, on/off, true/false type states.

# 7. NONE TYPE
#    - None: represents the intentional ABSENCE of a value — not zero, not
#      an empty string, but literally "nothing here yet." Commonly used as
#      a default/placeholder before real data is available (e.g. a database
#      connection that hasn't been established yet).
#    - Important distinctions:
#         ""  (empty string) -> a string that exists but contains zero characters
#         " " (whitespace string) -> a string containing one or more spaces
#         None -> no value/object exists at all
#      These three are NOT the same thing, even though they can all "look
#      empty" at a glance.


# ==============================================================================
# 4. TYPE CONVERSION (CASTING) & TYPE CHECKING
# ==============================================================================

# TYPE CONVERSION (also called "casting") means manually converting a value
# from one data type to another using functions like int(), float(), str().
#   int("21")     -> 21          (string to int)
#   str(21)       -> "21"        (int to string, often needed before
#                                 concatenating with + into another string)
#   float(5)      -> 5.0         (int to float)
#   float("99.99")-> 99.99       (string to float)
#
# TRUNCATION WARNING: converting a float to an int does NOT round the
# number — it completely CHOPS OFF (drops) the decimal part.
#   int(7.9)  -> 7   (not 8!)
#   int(-4.75)-> -4  (truncates toward zero)

# CHECKING A VARIABLE'S TYPE
# type(variable) -> tells you the exact class/type of a variable.
#   print(type(21))     -> <class 'int'>
#   print(type(21.0))   -> <class 'float'>
#
# isinstance(variable, type) -> a STRUCTURAL type check. Returns True/False
# depending on whether the variable belongs to a given type "box." Useful
# inside conditions (if isinstance(x, int): ...).
#   isinstance(5, int)        -> True
#   isinstance(5.0, int)      -> False (it's stored as a float, not an int)
# isinstance() also accepts a TUPLE of types to check against several
# possibilities at once:
#   isinstance(99.9, (float, int)) -> True (it matches float)

# float.is_integer() — A DIFFERENT KIND OF CHECK (VALUE, not TYPE)
# This method checks whether a float's mathematical VALUE has an empty
# fractional part (ends in .0) — it does NOT check the storage type.
#   (5.0).is_integer() -> True  (whole number value, even though it's a float)
#   (5.5).is_integer() -> False (has a real fraction)
# WARNING: this method only exists on floats in most Python versions;
# calling it on a plain int can raise an error (this was fixed to work on
# ints too starting from Python 3.12).
#
# THE TWO GOLDEN RULES OF NUMERIC VALIDATION:
#   Rule 1 (isinstance) -> use when you care about the STORAGE type/box.
#   Rule 2 (is_integer) -> use when you care about the VALUE inside a float.
# A common validation "pipeline" checks structural type FIRST, then
# mathematical value SECOND:
#   if isinstance(x, float) and x.is_integer():
#       # safe to treat x as a clean whole number


# ==============================================================================
# 5. NUMBERS & MATH OPERATORS
# ==============================================================================

# BASIC ARITHMETIC OPERATORS
#   +  addition
#   -  subtraction
#   *  multiplication

# THE TWO TYPES OF DIVISION (an important distinction in Python)
#   /  TRUE DIVISION  -> ALWAYS returns a float, even if the numbers divide
#                        evenly. Example: 15 / 4 -> 3.75 ; 10 / 2 -> 5.0
#   // FLOOR DIVISION -> divides and then rounds DOWN to the nearest whole
#                        number, chopping off any remainder/decimal.
#                        Example: 15 // 4 -> 3

# MODULO (%) — THE REMAINDER OPERATOR
# Returns only what is "left over" after a division.
#   15 % 4 -> 3   (because 4 goes into 15 three whole times, using up 12,
#                  and 15 - 12 leaves a remainder of 3)
# Very useful for checking things like "is this number even or odd?"
# (number % 2 == 0 means even).

# EXPONENTIATION (**)
# Raises a number to the power of another.
#   15 ** 2 -> 225  (15 squared)

# OPERATOR PRECEDENCE (ORDER OF OPERATIONS — similar to PEMDAS/BODMAS
# from math class)
# Python evaluates a mixed expression in this strict order:
#   1. Parentheses ()
#   2. Exponents **
#   3. Multiplication *, Division /, Floor Division //, Modulo %
#      (evaluated left to right)
#   4. Addition +, Subtraction - (evaluated left to right)
# Example: 5 + 3 * 2 -> 11 (multiplication happens before addition)
# Example: (5 + 3) * 2 -> 16 (parentheses force addition to happen first)

# AUGMENTED ASSIGNMENT OPERATORS (shortcuts to update a variable using its
# own current value)
#   score += 5   is shorthand for   score = score + 5
#   score -= 10  is shorthand for   score = score - 10
#   score *= 2   is shorthand for   score = score * 2
# (The same shortcut pattern also works for /=, //=, %=, **=)

# OPERATOR OVERLOADING — SAME SYMBOL, DIFFERENT MEANING
# In Python, an operator's behavior can change depending on the data types
# involved. This is called "operator overloading."
#   "404" * 3   -> "404404404"  (string * int = REPEATS the text 3 times)
#   404 * 3     -> 1212         (int * int = normal MATHEMATICAL multiplication)
# The + operator behaves similarly: adding two numbers does math, but "+"
# between two strings CONCATENATES (joins) them together instead.

# COMPLEX NUMBERS
# Built using the complex(real, imaginary) constructor, or written directly
# with a trailing j: 3 + 5j
#   complex(15, 22) -> (15+22j)
# Rarely needed for everyday programming, but useful in engineering/science
# contexts (e.g. representing AC electrical signals, vectors with 2 parts).

# BUILT-IN NUMBER FUNCTIONS: abs() AND round()
# abs(x) — ABSOLUTE VALUE: the distance of a number from zero on the number
# line. Distance is never negative, so abs() simply removes any minus sign.
# It preserves the input's type (an int stays an int, a float stays a float).
#   abs(-8)    -> 8
#   abs(-4.75) -> 4.75
#
# round(number, ndigits) — rounds to the nearest whole number, or to a
# specific number of decimal places if ndigits is given.
#   round(3.2) -> 3   (closer to 3)
#   round(3.8) -> 4   (closer to 4)
#
# THE ".5 TRAP" — BANKER'S ROUNDING:
# When a number falls EXACTLY halfway between two integers (ends in .5),
# Python does NOT always round up — it rounds to the nearest EVEN number
# instead. This is intentional: it removes statistical bias when rounding
# is done repeatedly across large datasets (e.g. financial or scientific
# calculations), since always rounding .5 up would slightly inflate results
# over many operations.
#   round(2.5) -> 2  (2 is the nearest even number)
#   round(3.5) -> 4  (4 is the nearest even number)
#
# Using the second argument gives decimal precision:
#   round(2.8764, 2) -> 2.88
#   round(2.8764, 3) -> 2.876


# ==============================================================================
# 6. THE math MODULE
# ==============================================================================

# math is a STANDARD MODULE — pre-installed with Python but not automatically
# loaded into memory, so it must be explicitly imported before use:
#   import math
# Once imported, its features are accessed with a dot: math.function_name()

# SCIENTIFIC CONSTANTS
#   math.pi   -> 3.14159...  the ratio of a circle's circumference to its diameter
#   math.e    -> 2.71828...  Euler's number, the base of natural growth/logarithms
#   math.tau  -> 6.28318...  a full circle's turn constant (tau = 2 * pi)
#   math.inf  -> a representation of mathematical infinity
#   math.nan  -> "Not a Number," used to represent missing/corrupted numeric data

# ADVANCED ROUNDING & SIGNS
#   math.ceil(x)  -> always rounds UP to the next whole number
#   math.floor(x) -> always rounds DOWN to the next whole number
#   math.trunc(x) -> chops off the decimal completely (same effect as int())
#   math.fabs(x)  -> absolute value, but always returns a float result

# POWERS, ROOTS, AND LOGARITHMS
#   math.sqrt(x)     -> square root, returns a float
#   math.isqrt(x)    -> integer square root, truncates the result down to an int
#   math.pow(x, y)   -> raises x to the power y, returns a float
#   math.log(x, base)-> logarithm with a custom base (if no base is given,
#                        it defaults to the natural log, base e)
#   math.log2(x)     -> shortcut for logarithm base 2
#   math.log10(x)    -> shortcut for logarithm base 10

# NUMBER THEORY FUNCTIONS
#   math.factorial(n) -> n! = n * (n-1) * (n-2) * ... * 1
#   math.gcd(a, b)     -> Greatest Common Divisor of two numbers
#   math.lcm(a, b)     -> Least Common Multiple of two numbers
#   math.isclose(a, b) -> safely checks if two floats are "close enough" to
#                          be considered equal, working around a quirky
#                          computer-science issue where floating-point math
#                          isn't always perfectly precise (for example,
#                          0.1 + 0.2 == 0.3 actually evaluates to False in
#                          raw comparison due to how computers store
#                          decimals in binary — isclose() solves this)

# TRIGONOMETRY (expects RADIANS, not degrees!)
#   math.radians(degrees) -> converts a degree value into radians
#   math.degrees(radians) -> converts a radian value back into degrees
#   math.sin(x), math.cos(x) -> standard trigonometric functions, expecting
#                                 the angle x in radians

# BUILT-IN min()/max() VS. MATH MODULE'S fmin()/fmax()
# The core built-in functions max() and min() work globally, without any
# import, on raw values or entire iterables (like lists).
#   max(10, 20, 5)         -> 20
#   min([45.9, 12.5, 89.0])-> 12.5
# The math module's specialized math.fmax() and math.fmin() do the same
# comparison, but they safely IGNORE 'nan' values instead of crashing or
# producing unpredictable results — useful when working with messy,
# real-world numeric data that might contain missing/invalid entries.


# ==============================================================================
# 7. THE random MODULE
# ==============================================================================

# random is a built-in module that generates "PSEUDO-RANDOM" numbers — not
# truly random in a philosophical sense, but generated using a mathematical
# formula starting from a hidden internal starting value called a "seed."
# For everyday programming purposes, the output behaves exactly like real
# randomness.
#   import random

# GENERATING RANDOM NUMBERS
#   random.randint(start, stop) -> a random INTEGER; BOTH boundaries are
#                                    INCLUDED in the possible outcomes.
#   random.random()              -> a random FLOAT between 0.0 (inclusive)
#                                    and 1.0 (exclusive)
#   random.uniform(start, stop)  -> a precise random FLOAT within a custom range

# WORKING WITH SEQUENCES (lists/strings)
#   random.choice(seq)   -> READ-ONLY: randomly picks exactly one item from
#                            a list/string, without changing the original.
#   random.shuffle(list) -> DESTRUCTIVE/IN-PLACE: permanently reorders the
#                            actual list you pass in (there is no separate
#                            "shuffled copy" returned — the original changes).

# REPEATABLE RANDOMNESS: THE SEED
#   random.seed(value) -> locks the random number generator's internal
#                          starting pattern. It does NOT force the output to
#                          equal the seed value itself — it forces the exact
#                          SEQUENCE of "random" results that follow to be
#                          identical every single time the script is run
#                          with that same seed. This is extremely useful for
#                          testing and reproducible experiments.


# ==============================================================================
# 8. STRINGS — FULL REFERENCE
# ==============================================================================

# THE GOLDEN RULE OF STRINGS: IMMUTABILITY
# Strings are IMMUTABLE — once a string object is created in memory, it can
# never be altered in place. Any method that appears to "modify" a string
# (like .upper() or .replace()) actually builds and returns a BRAND NEW
# string object; the original string is left completely untouched unless
# you explicitly re-assign the variable to the new result.
#   text = "iitm"
#   text.upper()          -> creates "IITM" but doesn't save it anywhere!
#   print(text)           -> still prints "iitm"
#   text = text.upper()   -> NOW text is permanently updated to "IITM"

# STRING INDEXING (grabbing a single character)
# Every character in a string has a position number, starting from 0 for
# the first character, called its "index."
#   Positive indexing counts from the left, starting at 0.
#   Negative indexing counts from the right, starting at -1 (the last char).
#     text = "Python"
#     text[0]  -> 'P' (first character)
#     text[-1] -> 'n' (last character)

# STRING SLICING (extracting a chunk/substring)
# Syntax: string[start:stop] — the 'start' index IS included, but the
# 'stop' index is EXCLUDED (the slice stops one position before it).
#     text[0:4]  -> characters at index 0,1,2,3 (NOT 4)
#     text[:3]   -> leaving 'start' empty defaults to the very beginning
#     text[2:]   -> leaving 'stop' empty goes all the way to the end
#     text[:]    -> leaving both empty copies the entire string
# Slicing also supports a third value for STEP: string[start:stop:step]
#     numbers[::2]  -> every 2nd character across the whole string
#     text[::-1]    -> a NEGATIVE step of -1 walks backward, giving an
#                       instant and very common trick to REVERSE a string

# CASE CONVERSION METHODS
#   .upper()      -> converts ALL characters to uppercase
#   .lower()      -> converts ALL characters to lowercase
#   .title()      -> capitalizes the first letter of EVERY word
#   .capitalize() -> capitalizes ONLY the very first character of the string
#   .swapcase()   -> flips the case of every character (upper<->lower)

# CLEANUP METHODS (removing unwanted whitespace)
#   .strip()  -> removes whitespace from BOTH ends
#   .lstrip() -> removes whitespace ONLY from the left side
#   .rstrip() -> removes whitespace ONLY from the right side
# All three can also take an argument specifying exactly which character(s)
# to strip instead of whitespace, e.g. text.strip("*")

# PADDING & ALIGNMENT
#   .center(width, char) -> centers the string within a given total width,
#                            padding extra space with the given character
#   .ljust(width, char)  -> left-aligns the string, padding the right side
#   .rjust(width, char)  -> right-aligns the string, padding the left side
#   .zfill(width)        -> pads a numeric-looking string with leading
#                            zeros until it reaches the given width
#                            (e.g. "42".zfill(5) -> "00042")

# SEARCHING & COUNTING
#   .count(sub)   -> counts how many times a substring appears
#   .find(sub)    -> returns the LOWEST index where a substring is found,
#                     or -1 if it is NOT found (never raises an error)
#   .rfind(sub)   -> like find(), but searches from the right, returning the
#                     HIGHEST (rightmost) matching index
#   .index(sub)   -> works exactly like find(), BUT raises a ValueError
#                     (crashes the program) if the substring is missing —
#                     use with caution, or wrap in error handling
#   .rindex(sub)  -> like rfind(), but also raises ValueError if missing

# REPLACING & SPLITTING
#   .replace(old, new)     -> replaces ALL occurrences of old with new
#   .split(delimiter)      -> breaks a string into a LIST of pieces, cut at
#                              every occurrence of the delimiter
#   .split(delimiter, n)   -> limits splitting to at most n cuts from the left
#   .rsplit(delimiter, n)  -> like split, but counts/limits cuts from the RIGHT
#   .splitlines()          -> splits a string into a list at every line break
#   .partition(sub)        -> splits at the FIRST match only, returning a
#                              3-item tuple: (before, match, after)
#   .rpartition(sub)       -> same idea, but splits at the LAST match

# JOINING A LIST BACK INTO A STRING
#   "separator".join(list_of_strings) -> combines list items into one string,
#                                          placing the separator between each
#     " - ".join(["Coding", "Reading"]) -> "Coding - Reading"

# BOOLEAN VALIDATION METHODS (all return True or False)
#   .isdigit()      -> True if ALL characters are digits (0-9)
#   .isalpha()      -> True if ALL characters are letters
#   .isalnum()      -> True if ALL characters are letters AND/OR numbers
#   .isnumeric()    -> True if numeric (broader than isdigit — also covers
#                       things like fractions or certain numeral systems)
#   .isdecimal()    -> True only for strict base-10 decimal digit characters
#   .isidentifier() -> True if the string would be a legal Python variable
#                       name
#   .islower()      -> True if all cased characters are lowercase
#   .isupper()      -> True if all cased characters are uppercase
#   .istitle()      -> True if the string follows title-case rules
#   .isspace()      -> True if the string contains ONLY whitespace characters
#   .isprintable()  -> False if the string contains invisible/control
#                       characters like newlines or tabs

# PREFIX & SUFFIX CHECKS
#   .startswith(sub) -> True if the string begins with the given text
#   .endswith(sub)   -> True if the string ends with the given text
#   .removeprefix(p) -> removes p from the start, only if present
#   .removesuffix(s) -> removes s from the end, only if present

# ADVANCED: CHARACTER TRANSLATION
#   str.maketrans(from_chars, to_chars) -> builds a translation "map" table
#   "text".translate(table)             -> applies that table, swapping each
#                                            matched character in one pass
#     table = str.maketrans("ae", "13")
#     "apple tree".translate(table) -> "1ppl3 tr33"

# METHOD CHAINING
# Because string methods return new strings, you can call multiple methods
# back-to-back in a single line — the result of each method feeds directly
# into the next, like an assembly line. This avoids creating many messy
# intermediate variables.
#   text.strip().replace(" ", "-").upper()
# is equivalent to doing strip, then replace, then upper as three separate
# steps, but in one clean expression.

# STRING CONCATENATION & REPETITION
#   "a" + "b"  -> joins ("concatenates") two strings into one: "ab"
#   "ab" * 3   -> repeats the string 3 times: "ababab"

# f-STRINGS (FORMATTED STRING LITERALS) — the modern way to build strings
# Placing an f (or F) directly before the opening quote lets you inject
# variables, numbers, or even full expressions directly inside curly
# braces { } — no need for manual concatenation with +.
#   name, age = "Vinita", 21
#   print(f"My name is {name} and I am {age} years old.")
# Rules to remember:
#   - the f must come right before the opening quote
#   - variables/expressions go inside { }
#   - everything must sit inside ONE pair of quotes
#   - you can put actual math or method calls inside the braces:
#       f"{price - discount}"      -> does the subtraction
#       f"{name.upper()}"          -> calls a method
#   - decimal formatting: f"{cgpa:.2f}" -> shows exactly 2 decimal places
#   - to print a LITERAL curly brace, double it up: {{ and }}
#   - \n also works inside f-strings for multi-line output

# THE in OPERATOR FOR STRINGS
# The easiest way to check if a word/character exists inside a string:
#   "fun" in "python is fun" -> True

# print() RETURNS None — AN IMPORTANT GOTCHA
# print() only DISPLAYS text on the screen; it does not hand back
# ("return") any usable value. If you accidentally do:
#   result = print("hello")
# then result will be None, NOT the printed text. Never use print() inside
# a math equation, condition, or variable assignment where you actually
# need the value.


# ==============================================================================
# 9. THE input() FUNCTION
# ==============================================================================

# input("prompt message") pauses the program and waits for the person using
# it to type something and press Enter. Whatever they type is captured and
# returned.
#
# CRITICAL RULE: input() ALWAYS returns a STRING, no matter what the person
# actually types — even if they type numbers like "25", Python still sees
# it as the text "25", not the number 25.
#   age = input("Enter your age: ")   -> age is a str, even if they typed 25
#
# To use it as a real number, you must manually convert it:
#   age = int(input("Enter your age: "))     -> for whole numbers
#   height = float(input("Enter height: "))  -> for decimal numbers
#
# input() is commonly combined with f-strings to build interactive prompts
# and greetings, and multiple input() calls can be chained one after another
# to collect several pieces of information in sequence.


# ==============================================================================
# 10. BOOLEANS & OPERATORS
# ==============================================================================

# THE bool TYPE
# Only two values exist: True and False (note the capital letters — "true"
# and "false" lowercase are NOT valid in Python).

# bool() — CONVERTING ANY VALUE TO TRUE/FALSE ("TRUTHY" vs "FALSY")
# Every value in Python can be evaluated as True or False in a boolean
# context, even if it isn't literally a bool.
#   FALSY values (evaluate to False): 0, 0.0, None, "" (empty string),
#                                      [] (empty list), {} (empty dict),
#                                      set() (empty set), False
#   TRUTHY values: basically everything else, including any non-empty
#                  string, non-zero number, or non-empty collection.
# This means you can write `if some_list:` instead of the longer
# `if len(some_list) > 0:` — Python treats a non-empty list as truthy
# automatically.

# any() AND all() — CHECKING MULTIPLE VALUES AT ONCE
#   any(iterable) -> True if AT LEAST ONE element is truthy
#   all(iterable) -> True ONLY IF EVERY element is truthy
# These are extremely useful for validation, e.g. checking that at least
# one of several optional fields (email, phone) has been filled in, or that
# every required field is non-empty.

# COMPARISON OPERATORS (always evaluate to True or False)
#   ==  equal to
#   !=  not equal to
#   <   less than
#   >   greater than
#   >=  greater than or equal to
#   <=  less than or equal to
# Python also allows CHAINED comparisons in one readable expression:
#   18 <= age <= 29   -> checks that age is between 18 and 29 (inclusive)

# LOGICAL OPERATORS (combine multiple True/False conditions)
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips/reverses a True/False result

# MEMBERSHIP OPERATORS
#   in     -> True if a sequence/collection contains the given value
#   not in -> True if it does NOT contain the given value

# IDENTITY OPERATORS: is / is not — A CRITICAL DISTINCTION FROM ==
#   ==  checks whether two values are EQUAL (same content)
#   is  checks whether two variables point to the exact SAME OBJECT in
#       computer memory (identity, not just equal content)
#     list_a = [1, 2, 3]
#     list_b = list_a          # both names now point to the SAME list object
#     list_c = [1, 2, 3]       # a separate, brand-new list with equal content
#     list_a == list_c  -> True  (same values)
#     list_a is list_c  -> False (different objects in memory)
#     list_a is list_b  -> True  (literally the same object)
# This distinction matters a lot when copying data structures (see the
# copying section under Lists).

# OPERATOR PRECEDENCE FOR LOGICAL OPERATORS: "NOT, AND, OR"
# Python evaluates logical operators strictly in this priority order:
#   1. not  (highest priority — evaluated first)
#   2. and
#   3. or   (lowest priority — evaluated last)
# Example without parentheses:
#   True or False and False
#   -> 'and' is evaluated first: False and False -> False
#   -> then: True or False -> True
#   Final result: True
#
# OVERRIDING PRECEDENCE WITH PARENTHESES
# Just like in math class, parentheses force Python to evaluate that part
# first, which also makes the intent of your code much clearer to read.
#   (True or False) and False
#   -> bracket evaluated first: True
#   -> then: True and False -> False
#
# BEST PRACTICE FOR READABILITY: even when precedence rules would give the
# correct answer without parentheses, adding them explicitly around related
# logic makes real-world conditions (like access-control checks) far less
# error-prone and easier for humans to read at a glance:
#   can_access = is_admin or (has_subscription and is_active)

# SHORT-CIRCUIT EVALUATION
# Python is "smart" about evaluating combined conditions and stops early
# whenever the final answer is already guaranteed:
#   - for 'and': if the FIRST value is already False, Python skips
#     evaluating everything after it (since the whole expression must be
#     False no matter what comes next).
#   - for 'or': if the FIRST value is already True, Python skips evaluating
#     everything after it (since the whole expression is already True).
# This is more than just a shortcut for speed — it means an expensive or
# slow operation placed later in the condition (like a database check or
# network call) may never even run if an earlier, cheaper check already
# decided the outcome. This is a common real-world performance technique.


# ==============================================================================
# 11. CONDITIONAL STATEMENTS
# ==============================================================================

# THE BASIC if / elif / else STRUCTURE
# Python uses INDENTATION (consistently 4 spaces is the convention) to mark
# which lines belong inside a code block, instead of curly braces {} like
# some other languages use.
#   if condition:
#       # runs only if condition is True
#   elif another_condition:   # short for "else if" — checked only if the
#       # runs if the first condition was False but this one is True     first
#                                                                          one
#                                                                          was
#                                                                          False
#   else:
#       # runs if none of the above conditions were True
# Python checks conditions top to bottom and stops at the FIRST one that is
# True — later elif/else blocks are then skipped entirely.

# NESTED CONDITIONALS
# An if statement can be placed inside another if statement's block, letting
# you check a second condition only after the first one is confirmed true.
# Useful, but should be used sparingly — too much nesting quickly becomes
# hard to read.

# THE TERNARY OPERATOR (a one-line conditional expression)
# A shortcut for a simple if-else that assigns one of two values.
#   Syntax: value_if_true if condition else value_if_false
#     status = "Adult" if age >= 18 else "Minor"
# This does the exact same job as a 3-4 line if/else block, just condensed
# onto one readable line — best used only for genuinely simple choices.

# TRUTHY/FALSY VALUES INSIDE if STATEMENTS
# You don't always need an explicit comparison operator. Python will
# directly evaluate a value's truthiness inside an if condition:
#   if cart:              # True automatically if the list is NOT empty
#       print("proceed")
#   else:
#       print("cart is empty")

# STRUCTURAL PATTERN MATCHING: match / case (Python 3.10 and newer)
# Acts like a "switch" statement found in many other languages — ideal for
# cleanly matching a variable against several specific possible values.
#   match value:
#       case 200:
#           ...
#       case 400:
#           ...
#       case 500 | 503:      # the | acts like "or" inside a single case,
#           ...               # matching either value
#       case _:               # underscore is a WILDCARD — a catch-all,
#           ...                # exactly like a final 'else'

# COMBINING CONDITIONS WITH and / or / not
# Real-world validation logic (like checking if an email address is
# correctly formatted) often chains several elif conditions together,
# each checking one specific rule (not empty, contains "@", ends with a
# valid domain, correct length, doesn't start/end with a symbol, etc.),
# falling through to a final "else: valid" only if every check passes.


# ==============================================================================
# 12. LOOPS
# ==============================================================================

# WHY LOOPS EXIST
# Loops are control structures used to repeat a block of code multiple
# times instead of writing the same instructions over and over manually.

# FOR LOOP — DEFINITE ITERATION
# Used when you know (or Python can determine) how many times to repeat —
# it automatically runs once for every item in a sequence (a list, string,
# tuple, range, etc.).
#   Syntax:
#     for element in iterable_sequence:
#         # code to repeat for each element
# Python handles initializing, updating, and stopping the loop variable
# automatically as it walks through the sequence — you never manually
# manage a counter.

# THE range() FUNCTION — GENERATING NUMBER SEQUENCES FOR LOOPS
#   range(stop)              -> counts from 0 up to (but EXCLUDING) stop
#   range(start, stop)       -> counts from start up to (but excluding) stop
#   range(start, stop, step) -> counts by increments/decrements of step
#     range(3)         -> 0, 1, 2
#     range(5, 8)       -> 5, 6, 7
#     range(10, 21, 5)  -> 10, 15, 20

# WHILE LOOP — INDEFINITE ITERATION
# Used when the exact number of repetitions is unknown ahead of time — it
# keeps running for as long as a given condition stays True.
#   Syntax:
#     while condition_is_true:
#         # code to repeat
#         # something MUST eventually make the condition False, or update a
#         # counter — otherwise this becomes an INFINITE LOOP that never stops!
# Unlike a for loop, a while loop requires MANUAL state management: you
# must initialize a tracking variable before the loop starts, and manually
# update it somewhere inside the loop body.

# FOR LOOP vs WHILE LOOP — KEY DIFFERENCES
#   1. Iteration type: for = definite (fixed count based on a sequence's
#      length); while = indefinite (runs based on a changing condition,
#      count unknown ahead of time).
#   2. State management: for = automatic (Python manages it internally);
#      while = manual (you control the counter yourself).
#   3. Infinite loop risk: for = very safe, naturally ends when the
#      sequence runs out; while = higher risk if you forget to update the
#      condition variable.
#   4. Best use cases: for = traversing known collections/ranges;
#      while = waiting for events, tracking changing states (like a game
#      loop, or repeatedly asking for input until a person types something
#      valid).

# COMMON while LOOP PATTERNS
#   - Manual counter: initialize a variable, check it in the while
#     condition, and update it inside the loop body each pass.
#   - while True: with an internal break — deliberately starts an infinite
#     loop, relying entirely on an if condition inside to break out when a
#     specific event happens (e.g. the person finally types the right
#     answer).
#   - Attempt-limiting / retry pattern — combines while True with a counter
#     that tracks how many attempts have been made, breaking out either
#     when the task succeeds OR when a maximum number of attempts is
#     reached (e.g. "you have 3 tries to enter the right password").

# LOOP CONTROL MODIFIERS: break, continue, pass
#   break    -> instantly and completely exits/aborts the loop, skipping
#               any remaining iterations entirely.
#   continue -> skips the REST of the current iteration only, and jumps
#               straight to checking the next item/iteration.
#   pass     -> a silent placeholder that does absolutely nothing. Used
#               when Python's syntax requires a code block to not be empty,
#               but you don't want any action to actually happen there yet
#               (helps avoid syntax errors while still writing/planning code).

# THE LOOP else BLOCK (a feature many other languages don't have!)
# A for or while loop can have an else block attached. This else runs ONLY
# IF the loop completes its ENTIRE sequence naturally, WITHOUT ever hitting
# a break statement partway through.
#   for item in items:
#       if item == target:
#           print("Found it!")
#           break
#   else:
#       print("Never found it in the whole list.")
# This pattern is extremely useful for "search" logic: the else branch acts
# as an automatic "not found" message, only firing if break never triggered.
# It's also useful for detecting duplicates, validating that "all items in
# a list passed a check," etc.

# print() end AND sep PARAMETERS (loop output control)
#   sep (separator) -> controls what character is inserted BETWEEN multiple
#                       comma-separated items in a single print() call
#                       (default is one space).
#   end (line-ender) -> controls what gets added at the very end of a
#                        print() call instead of the default newline
#                        character. Setting end=" " lets a loop print
#                        several items on the SAME line, one after another.

# NESTED LOOPS
# A NESTED LOOP is any loop (for or while) placed entirely inside the body
# of another loop. The inner loop runs its COMPLETE cycle of iterations for
# every single iteration of the outer loop.
# A NESTED FOR LOOP specifically places a for loop inside another for loop
# — commonly used to:
#   - work through multi-dimensional data (like a grid, matrix, or table)
#   - generate every possible COMBINATION between two separate sequences
#     (e.g. pairing every color with every size to list all product variants)
# Extending this to THREE nested loops lets you walk through 3-level
# hierarchical/tree-shaped data, such as:
#   - Year -> Month -> Day (a full calendar breakdown)
#   - Database Table -> Column -> Row (scanning every cell in every table)
#   - Cloud Storage Container -> Folder -> File (processing every file in
#     every folder of every storage container)
# In each case, the OUTERMOST loop moves the SLOWEST (changes least often),
# and the INNERMOST loop moves the FASTEST, fully completing its entire
# cycle before the loop one level up even advances to its next item.


# ==============================================================================
# 13. LISTS
# ==============================================================================

# WHAT IS A LIST?
# An ORDERED, MUTABLE (changeable) collection that allows duplicate values.
# Written with square brackets: [item1, item2, item3]
# "Ordered" means items keep the position they were placed in, and can be
# accessed by that position (index) reliably.

# CREATING LISTS
#   empty = []                      -> an empty list
#   letters = ["a", "b", "c"]       -> a list literal
#   x = list()                      -> another way to make an empty list
#   x = list("hello")               -> converts a string into a list of its
#                                       individual characters: ['h','e','l',...]
#   x = list(range(1, 51))          -> converts a range into an actual list
#                                       of numbers
# A list can also hold MIXED data types together, including other lists,
# dictionaries, numbers, and strings all in the same list.

# NESTED LISTS (LISTS OF LISTS) — OFTEN CALLED A "MATRIX"
# A list where some or all elements are themselves lists, commonly used to
# represent grid/table-like data (rows and columns).
#   matrix = [[1,2,3],[4,5,6],[7,8,9]]
# To read a value, you index TWICE: first into the outer list to pick a
# row, then again into that row to pick a specific item.
#   matrix[1][1] -> picks row index 1, then item index 1 within that row -> 5
# Slicing also works at each level:
#   matrix[0][1:] -> slices within just the first row

# LIST INDEXING & SLICING
# Works exactly like string indexing/slicing (see Section 8) — positive
# indexing from the left starting at 0, negative indexing from the right
# starting at -1, and start:stop:step slicing rules all apply identically.

# UNPACKING LISTS
# Unpacking means assigning each item of a list directly to its own
# separate variable, all in one line.
#   name, age, city = ["Vinita", 21, "Indore"]
# RULES:
#   1. The number of variables on the left must match the number of items
#      (unless you use * — see below).
#   2. You can unpack ANY sequence type this way — not just lists, but also
#      tuples and strings.
#
# REST COLLECTION WITH ASTERISK (*)
# Placing a * before one variable name lets it "soak up" any extra,
# unmatched items into a list, while the other variables take exactly one
# item each.
#   name, *details, happiness = my_list
#   -> name gets the first item, happiness gets the last item, and
#      "details" becomes a LIST containing everything left in between.
# Only ONE asterisk is allowed per unpacking statement, but you can name
# that "catch-all" variable anything you like.
#
# SKIPPING VALUES WITH UNDERSCORE (_)
# By convention, using _ as a variable name signals "I don't care about
# this value, I'm intentionally throwing it away."
#   name, _, country, _ = my_list   -> only name and country are actually used
# You can also combine * and _ together:
#   first, *_, last = my_list   -> grabs only the first and last items,
#                                   discarding everything in the middle

# ANALYZING LIST DATA (BUILT-IN FUNCTIONS THAT WORK ON ANY ITERABLE)
#   max(list)  -> the largest value
#   min(list)  -> the smallest value
#   len(list)  -> the number of items
#   sum(list)  -> adds up all numeric items
#   all(list)  -> True only if every item is truthy
#   any(list)  -> True if at least one item is truthy
# Remember from Section 10: empty strings, empty lists, empty tuples, and
# empty dicts are all considered FALSY when checked with all()/any().

# COUNTING & LOCATING ITEMS
#   list.count(value) -> how many times a value appears
#   list.index(value) -> the index of the FIRST matching occurrence
#                         (raises an error if the value isn't in the list)

# MEMBERSHIP CHECKS
#   value in list      -> True if the value exists somewhere in the list
#   value not in list  -> True if it does not exist

# COMPARING LISTS
#   ==  -> checks if two lists have the SAME VALUES in the same order
#   is  -> checks if two variables point to the exact SAME list object in
#          memory (see the identity operators explanation in Section 10)
#   <, >, etc. -> lists can be compared "lexicographically," meaning Python
#          compares them element by element from left to right, similar to
#          how words are alphabetically ordered.

# MUTATING METHODS (methods that change the list IN PLACE)
#   list.append(value)   -> adds one item to the END of the list
#   list.insert(i, value)-> inserts an item at a specific index position
#   list.extend(other)   -> adds every item FROM another iterable onto the
#                            end of the list (expanding it), as opposed to
#                            appending the whole other list as one single item
#   list.remove(value)   -> removes the FIRST matching value (errors if
#                            the value isn't found)
#   list.pop()            -> removes and returns the LAST item
#   list.pop(i)           -> removes and returns the item at a specific index
#   list.clear()          -> empties the list completely
#   list.sort()           -> sorts the list IN PLACE (permanently reorders
#                             the original list; returns None, not a new list!)
#   list.sort(reverse=True) -> sorts in descending order
#   list.reverse()        -> reverses the list's order in place

# sorted() vs .sort() — AN IMPORTANT DISTINCTION
#   list.sort()   -> changes the ORIGINAL list directly, returns None
#   sorted(list)  -> does NOT touch the original list; instead it returns
#                     a brand NEW, separately sorted list, leaving the
#                     original list completely unchanged
# The same distinction applies to:
#   list.reverse()  -> reverses in place, returns None
#   reversed(list)  -> returns a special "reversed iterator" object (not
#                       a list!) which must be wrapped in list(reversed(x))
#                       to actually see/use it as a normal list

# REFERENCE ASSIGNMENT vs. COPYING A LIST
# This is one of the most important — and most commonly misunderstood —
# concepts for beginners.
#   original = ['a','b','c']
#   copy_var = original       # this does NOT create a new list!
# Both "original" and "copy_var" now point to the exact SAME list object in
# memory. If you modify one (e.g. copy_var.append("x")), the change shows
# up through BOTH variable names, because there was only ever one list to
# begin with — just two labels pointing at it.
#
# SHALLOW COPY — an actual separate list, but only "one level deep"
#   copy_var = original.copy()   # creates a genuinely separate list object
# Now appending to copy_var will NOT affect original, because they are two
# different list objects. HOWEVER: if the list contains nested objects
# (like a list of lists), a shallow copy only duplicates the OUTER list —
# the inner nested lists are still shared/referenced between both copies.
# So modifying a nested inner list through one copy WILL still affect the
# "other" copy too, because that inner list itself was never truly duplicated.
#
# DEEP COPY — a truly independent copy at EVERY level
#   import copy
#   copy_var = copy.deepcopy(original)
# This recursively duplicates everything, including all nested lists,
# dictionaries, etc., so that the new copy is 100% independent of the
# original at every level, no matter how deeply nested the data is.
#
# RULE OF THUMB: for simple, "flat" one-dimensional lists (no nested lists
# inside), a shallow copy (.copy()) is perfectly sufficient. For anything
# with more than one dimension/nested structure, use copy.deepcopy() if you
# need the copies to be truly independent of each other.

# COMBINING LISTS
#   list1 + list2   -> creates a new list with all items from both, in order
#   list * n        -> repeats the entire list's contents n times
#   [list1, list2]  -> wraps both lists as two separate items inside a new
#                       outer list (a nested list, NOT a combined/flat one)
#   list1.extend(list2) -> adds list2's individual items onto the end of
#                            list1 directly (modifies list1 in place)

# zip() — PAIRING UP ITEMS FROM MULTIPLE ITERABLES
# zip() takes two or more iterables and pairs up their items by matching
# position: the 1st item of the first iterable with the 1st item of the
# second, the 2nd with the 2nd, and so on.
#   list(zip(["a","b","c"], [1,2,3])) -> [('a',1), ('b',2), ('c',3)]
# The result is a list of TUPLES. If the iterables are different lengths,
# zip() stops as soon as the SHORTEST one runs out of items (extra items in
# a longer iterable are simply ignored). zip() itself produces a special
# "zip object" (an iterator), so it must be wrapped in list() to view or
# use it as an actual list.

# ITERATORS AND ITERABLES (a conceptual note)
# An "iterable" is anything you can loop over (lists, strings, tuples,
# dicts, ranges, etc.). Certain functions like zip(), map(), filter(), and
# reversed() don't return a plain list directly — they return a special
# lightweight "iterator" object instead, which only produces its values
# when you actually loop over it or explicitly convert it with list(...).
# This is a memory-efficient design choice: the values aren't all
# calculated and stored at once, only as they are needed.

# enumerate() — GETTING BOTH THE INDEX AND THE VALUE WHILE LOOPING
#   for index, value in enumerate(my_list):
#       print(index, value)
# By default, indexing starts at 0, but you can choose a different starting
# number: enumerate(my_list, start=1)

# map() — TRANSFORMING EVERY ITEM IN AN ITERABLE
# Syntax: map(transformation_function, iterable)
# Applies a given function to EVERY item and returns an iterator of the
# results (again, wrap in list() to see them). It does NOT modify the
# original iterable at all — it produces entirely new transformed values.
#   list(map(str.upper, ["a","b","c"])) -> ['A','B','C']
#   list(map(int, ["1","2","3"]))       -> [1, 2, 3]

# filter() — KEEPING ONLY ITEMS THAT PASS A TEST
# Syntax: filter(test_function, iterable)
# Keeps only the items for which the given function returns a truthy
# result, discarding everything else. Also returns an iterator, so wrap
# with list() to view the results.
#   list(filter(str.isalpha, ["vinita","980","hello"])) -> ['vinita','hello']
# A very handy special case: filter(None, iterable) removes every FALSY
# value from an iterable automatically (empty strings, False, None, 0, etc.)
# without needing to write a custom test function at all — because passing
# None as the function tells filter() to just use each item's own
# truthiness directly as the test.

# isinstance() FOR FILTERING BY TYPE
# isinstance(object, type) checks whether a specific object matches a
# given data type — frequently combined with filter() or list
# comprehensions to keep only items of a certain type in a mixed-type list.


# ==============================================================================
# 14. TUPLES & SETS
# ==============================================================================

# DATA STRUCTURE COMPARISON AT A GLANCE
#   LIST  -> ordered, MUTABLE, duplicates allowed, accessed by index
#   TUPLE -> ordered, IMMUTABLE, duplicates allowed, accessed by index
#   SET   -> UNORDERED, mutable, duplicates automatically removed, NOT
#            indexed (no fixed position to access items by)

# TUPLES
# Written with round brackets: (10, 20, 30). Once created, a tuple's
# contents can never be changed, added to, or removed from — this
# immutability makes tuples a good choice for data that should be
# protected from accidental modification (e.g. fixed coordinates, days of
# the week).
# sorted(a_tuple) still works and returns the sorted result — but note that
# the OUTPUT of sorted() is always a plain LIST, even when the input was a
# tuple, because a tuple itself cannot be reordered/mutated to hold a
# sorted version of itself.

# SETS
# Written with curly braces (but WITHOUT key:value pairs, which is what
# distinguishes a set from a dictionary): {10, 20, 30}
# Key properties:
#   - UNORDERED: there is no guaranteed position/order to the items, and
#     printing a set may not show them in the order you typed them.
#   - Automatically removes duplicates: {10,20,30,10} becomes {10,20,30}
#   - NOT indexed: you cannot access set items by position (my_set[0] is
#     invalid), since there is no fixed order to index into.
#   - Mutable: individual items can be added or removed after creation
#     (though the set object itself is what changes, not any single item —
#     items inside a set must themselves be immutable types, like numbers
#     or strings).

# SET METHODS FOR ADDING/REMOVING ITEMS
#   set.add(value)       -> adds a single item (does nothing if it's already
#                             present, since duplicates aren't allowed)
#   set.update(iterable)  -> adds MULTIPLE items at once, taken individually
#                             from the given iterable (e.g. update("hy") adds
#                             'h' and 'y' as two separate characters, NOT
#                             the whole string "hy" as one single item)
#   set.remove(value)    -> removes a value; RAISES AN ERROR if that value
#                             doesn't exist in the set
#   set.discard(value)   -> removes a value if present, but does NOTHING
#                             (no error) if it's missing — a "safer" version
#                             of remove()
#   set.pop()            -> removes and returns some RANDOM item from the
#                             set (since sets have no defined order, there
#                             is no concept of "the first" or "the last" item)
# Set updates can also be done with an operator shortcut:
#   my_set |= {"new_item"}   -> equivalent to my_set.update({"new_item"})

# SET MATHEMATICAL OPERATIONS (based on real mathematical set theory)
#   set1.union(set2)                 or  set1 | set2
#       -> combines all unique items from both sets
#   set1.intersection(set2)          or  set1 & set2
#       -> only the items that exist in BOTH sets
#   set1.difference(set2)            or  set1 - set2
#       -> items that are in set1 but NOT in set2
#   set1.symmetric_difference(set2)  or  set1 ^ set2
#       -> items that exist in EITHER set, but NOT in both (the "non-
#          overlapping" items from each side)

# SET RELATIONSHIP CHECKS
#   set1.issubset(set2)   -> True if EVERY item in set1 also exists in set2
#   set1.issuperset(set2) -> True if set1 contains ALL items of set2 (the
#                             reverse relationship of issubset)
#   set1.isdisjoint(set2) -> True if the two sets share NO items at all in
#                             common (a completely non-overlapping pair)


# ==============================================================================
# 15. DICTIONARIES
# ==============================================================================

# WHAT IS A DICTIONARY?
# A collection that stores data as KEY-VALUE PAIRS, written with curly
# braces: {"key1": value1, "key2": value2}. Keys must be UNIQUE (no
# duplicate keys allowed — assigning to an existing key just overwrites its
# value) and must be an immutable type (typically a string or number).
# Values can be anything, including duplicates, and dictionaries maintain
# the order items were inserted in modern Python.

# ACCESSING VALUES
#   my_dict["key"]              -> returns the value for that key; RAISES
#                                    AN ERROR if the key does not exist
#   my_dict.get("key")          -> returns the value if the key exists,
#                                    otherwise returns None (does NOT crash)
#   my_dict.get("key", default) -> like above, but returns your chosen
#                                    fallback value instead of None if the
#                                    key is missing
# .get() is generally the SAFER choice whenever you're not 100% sure a key
# will be present (e.g. reading data from an external/unpredictable source).

# MEMBERSHIP CHECKS
#   "key" in my_dict      -> True if that key exists (checks KEYS by default,
#                              not values)
#   "key" not in my_dict  -> True if it does not exist

# VIEW OBJECTS — INSPECTING WHAT'S INSIDE A DICTIONARY
#   my_dict.keys()   -> a view of all the keys
#   my_dict.values() -> a view of all the values
#   my_dict.items()  -> a view of all key-value pairs, each as a tuple
#                         (key, value)

# ITERATING OVER A DICTIONARY
#   for key in my_dict:            -> loops over KEYS only by default
#       print(key, my_dict[key])   -> use the key to look up its value
#   for key, value in my_dict.items():  -> loops over BOTH at once, cleanly

# ADDING, UPDATING, AND REMOVING ENTRIES
#   my_dict["new_key"] = value      -> adds a new entry, OR updates it if
#                                        that key already existed
#   my_dict.update({"k1": v1, "k2": v2}) -> adds/updates MULTIPLE keys at once
#   my_dict.pop("key")               -> removes a key and RETURNS its value;
#                                         raises an error if missing
#   my_dict.pop("key", default)      -> like above, but returns a fallback
#                                         default instead of erroring if the
#                                         key isn't found
#   my_dict.popitem()                -> removes AND returns the MOST
#                                         RECENTLY added key-value pair as a
#                                         tuple (a "last in, first out" removal)

# dict.fromkeys() — BUILDING A DICTIONARY WITH A SHARED DEFAULT VALUE
#   dict.fromkeys(["a","b","c"], 0)
#   -> {"a": 0, "b": 0, "c": 0}
# Useful for quickly initializing a dictionary structure where every key
# should start out with the same placeholder/default value.

# BUILDING A NEW DICTIONARY FROM AN EXISTING ONE (FILTERING)
# A common pattern is looping through .items(), checking a condition, and
# only adding qualifying key-value pairs into a brand new empty dictionary
# — effectively "filtering" a dictionary the same way filter() works on a
# list.

# DICTIONARY COMPREHENSION
# A compact, one-line way to build a new dictionary directly from an
# existing iterable, optionally applying a transformation and/or filter
# condition — the dictionary equivalent of list comprehension (see
# Section 16).
#   { key_expr : value_expr for item in iterable if condition }
#   Example: keep only string values, and uppercase them:
#     { k: v.upper() for k, v in user.items() if isinstance(v, str) }


# ==============================================================================
# 16. FUNCTIONS
# ==============================================================================

# WHAT IS A FUNCTION?
# A function is a reusable, named block of code that performs a specific
# task, written once and then "called" (used) as many times as needed,
# instead of rewriting the same logic repeatedly.
#   def function_name(parameters):
#       # code to run
#   function_name(arguments)   # this is how you actually "call"/run it

# PARAMETERS vs. ARGUMENTS — A COMMON POINT OF CONFUSION
#   PARAMETER -> the placeholder NAME listed in the function's definition
#                (e.g. `text` in `def clean_text(text):`)
#   ARGUMENT  -> the ACTUAL VALUE you pass in when calling the function
#                (e.g. `"hello"` in `clean_text("hello")`)
# In short: parameters are defined, arguments are supplied.

# LOCAL VARIABLES vs. GLOBAL VARIABLES
#   GLOBAL variable -> created OUTSIDE any function, and can generally be
#                       accessed from anywhere in the program, including
#                       from inside functions (though modifying a global
#                       variable from inside a function requires special
#                       handling that goes beyond these basics).
#   LOCAL variable  -> created INSIDE a function, and can ONLY be accessed
#                       from within that same function. Once the function
#                       finishes running, its local variables disappear.
# This matters because using the same variable name in two different
# functions (or inside vs. outside a function) does NOT cause a conflict —
# each local variable exists in its own separate, temporary "scope."

# POSITIONAL ARGUMENTS vs. KEYWORD ARGUMENTS
#   POSITIONAL -> values are matched to parameters purely by the ORDER they
#                 are listed in the function call.
#     my_name("Vinita", "Patidar")  -> first_name="Vinita", last_name="Patidar"
#   KEYWORD    -> values are matched to parameters by explicitly naming
#                 which parameter each value belongs to, so ORDER no longer
#                 matters.
#     my_name(last_name="Patidar", first_name="Vinita")  -> same result
# MIXING both styles in one call is allowed, but positional arguments must
# always come FIRST, followed by keyword arguments — you cannot put a
# positional argument after a keyword argument in the same call.
# The NUMBER of arguments given must match the number of required
# parameters (unless default values or *args/**kwargs are used — see below).

# DEFAULT PARAMETER VALUES
# A parameter can be given a default value directly in the function
# definition. If the caller doesn't supply a value for it, Python
# automatically uses the default instead.
#   def student(class_, roll_no, school="DPS"):
#       ...
#   student(2, 201)              -> school defaults to "DPS"
#   student(2, 201, "St. Mary's")-> school is overridden
# RULE: all parameters WITHOUT a default value must be listed BEFORE any
# parameters that DO have a default value in the function definition.

# *args — ACCEPTING AN UNKNOWN NUMBER OF POSITIONAL ARGUMENTS
# When you don't know in advance how many values someone might want to
# pass in, prefixing a parameter name with a single asterisk collects ALL
# extra positional arguments into a TUPLE automatically.
#   def add_numbers(*args):
#       return sum(args)
#   add_numbers(1, 2, 3)          -> args becomes (1, 2, 3)
#   add_numbers(1, 2, 3, 4, 5, 6) -> args becomes (1, 2, 3, 4, 5, 6)
# Best used when all the extra values are conceptually SIMILAR/the same
# kind of thing (e.g. a list of numbers to add together).

# **kwargs — ACCEPTING AN UNKNOWN NUMBER OF KEYWORD ARGUMENTS
# Prefixing a parameter name with TWO asterisks collects any extra
# keyword arguments into a DICTIONARY automatically, where each argument's
# name becomes a key.
#   def user_profile(**kwargs):
#       print(kwargs)
#   user_profile(name="Vinita", age=21, country="India")
#   -> kwargs becomes {"name": "Vinita", "age": 21, "country": "India"}
# Best used when you want to accept a flexible set of DIFFERENTLY-NAMED
# pieces of information that may vary depending on the situation.

# return — SENDING A VALUE BACK OUT OF A FUNCTION
# The return statement hands a result back to wherever the function was
# called from, so it can be stored in a variable or used immediately.
#   def full_name(first, last):
#       return first.strip().lower() + " " + last.strip().lower()
#   result = full_name("Vinita ", " Patidar")
#   print(result)
# IMPORTANT: if a function has NO return statement at all (or the return
# line is skipped/commented out), Python automatically returns None by
# default — this is a common source of confusing bugs for beginners who
# expect some other value.
#
# A function CAN contain multiple return statements, usually inside
# different branches of an if/else — but as soon as ANY return statement
# executes, the function immediately stops running right there; any code
# written after that return inside the same function will never run.
#
# RETURNING MULTIPLE VALUES AT ONCE
# A function can return more than one value, separated by commas — Python
# automatically packages them together into a TUPLE behind the scenes.
#   def full_name(first, last):
#       return first.lower(), first.upper()
#   result = full_name("Vinita", "Patidar")  -> result is a tuple of 2 values

# CATEGORIES OF FUNCTIONS (a conceptual way to think about function design)
#   ACTION FUNCTION -> designed to DO something / cause an effect in the
#       system, rather than hand back a value. Example: writing a log
#       message to a file whenever some event happens.
#   TRANSFORMATION FUNCTION -> takes raw input data, processes/reshapes it
#       in some way, and returns the newly transformed result. Example:
#       cleaning up a messy email address and splitting it into a
#       structured dictionary of {username, domain}.
#   VALIDATION FUNCTION -> checks whether some condition/rule is satisfied,
#       and returns a simple True/False (boolean) result. Example:
#       checking whether a password meets minimum length/complexity rules.
#   ORCHESTRATOR FUNCTION -> doesn't do detailed work itself, but instead
#       controls the overall PROGRAM FLOW by calling several other,
#       smaller functions in the correct order — like a manager
#       coordinating a team, rather than doing every task personally.


# ==============================================================================
# 17. LAMBDA FUNCTIONS & LIST COMPREHENSION
# ==============================================================================

# LAMBDA FUNCTIONS — SHORT, ANONYMOUS, ONE-LINE FUNCTIONS
# A lambda is a compact way to write a very small function without using
# the full 'def' syntax and without giving it a permanent name (hence
# "anonymous"). It can only contain a SINGLE EXPRESSION (no multiple lines
# of logic, no separate return statement needed — the expression's result
# IS automatically the return value).
#   Syntax: lambda parameters : expression
#     double = lambda x: x * 2
#     print(double(6))     -> 12
# Lambdas can take multiple parameters, just like normal functions:
#     add_sub = lambda x, y, z: x + y - z
# Lambdas can contain conditional/boolean expressions too:
#     is_in_python = lambda i: i in "python"

# WHY USE LAMBDAS?
# They shine when you need a quick, "throwaway" function to pass directly
# into another function — most commonly map() and filter() — without the
# overhead of formally defining a full named function elsewhere just to
# use it once.

# LAMBDA + map() — TRANSFORMING DATA ON THE FLY
#   prices = ["$103.00", "$567.99"]
#   clean_price = lambda p: float(p.replace("$", ""))
#   list(map(clean_price, prices))            -> [103.0, 567.99]
#   list(map(lambda p: float(p.replace("$","")), prices))  -> same result,
#                                                              written inline

# LAMBDA + filter() — SELECTING DATA ON THE FLY
#   rent = [1000, 980, 120, 89]
#   list(filter(lambda x: x > 100, rent))    -> [1000, 980, 120]
# Lambdas are especially handy for filtering NESTED data structures, like a
# list of [name, score] pairs, by accessing an index inside the expression:
#   list(filter(lambda x: x[1] > 50, students))     # filter by score
#   list(filter(lambda x: x[0].startswith("m"), students))  # filter by name

# LIST COMPREHENSION — A COMPACT WAY TO BUILD NEW LISTS
# List comprehension lets you create a new list in a single, readable line,
# combining a loop and an optional condition together.
#   Syntax: [expression for item in iterable if condition]
#     result = [p for p in prices if p > 33]
# This is functionally equivalent to writing a full for loop that checks a
# condition and appends qualifying items to an empty list — but far more
# compact once you're comfortable reading the pattern.
# It's extremely common for cleaning/transforming a whole batch of data in
# one line, e.g. stripping whitespace, lowercasing, and replacing text
# across every item of a list of raw email addresses all at once:
#   cleaned = [x.strip().lower().replace("www.", "") for x in raw_emails]

# WHEN TO CHOOSE WHAT (a quick mental guide)
#   - Use a normal 'def' function for anything with multiple lines of logic,
#     or anything you plan to reuse by name in many places.
#   - Use a lambda for a small, single-expression, "use it right here, right
#     now" function — most often as an argument to map()/filter()/sorted().
#   - Use list/dict comprehension instead of a manual for-loop-and-append
#     pattern whenever you're building a new collection from an existing
#     one in a simple, readable way.

# ==============================================================================
# END OF NOTES
# ==============================================================================