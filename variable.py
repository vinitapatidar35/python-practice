# A variable in Python is a name used to store data in memory so it can be used and modified later in a program.
# How variables work in Python:
# A variable is like a container that stores data in memory.
# When you assign a value to a variable, Python stores that value and links it to the variable name.
# Whenever you use the variable, Python fetches the stored value from memory.

name , age , city = "vinita" , 21 , "Indore"
print(f"my name is :  {name} and i am {age} old .")
cgpa = 7.7
cgpa = int(cgpa)
print(cgpa)
print(type(name))
print(type(age))
print(type(city))
add = cgpa + 9.0
print(add)

# F-STRING COMPLETE NOTES
# =======================

# What is f-string?
# A way to put variables directly inside a string
# Just add 'f' before the opening quote

# BASIC SYNTAX:
# print(f"text {variable} text")

# -----------------------------------------------
# RULE 1 — Add 'f' before the quote
# -----------------------------------------------
print(f"Hello Vinita")        # ✅ f-string
# print("Hello Vinita")       # normal string - no variables

# -----------------------------------------------
# RULE 2 — Variables go inside { } curly brackets
# -----------------------------------------------
name = "Vinita"
age = 21
print(f"My name is {name}")   # ✅ correct
# print(f"My name is name")   # ❌ prints literally 'name'

# -----------------------------------------------
# RULE 3 — Everything inside ONE set of quotes
# -----------------------------------------------
# ✅ Correct
print(f"My name is {name} and I am {age} old.")
# ❌ Wrong
# print(f"My name is " {name} " and I am " {age})

# -----------------------------------------------
# MATH inside { }
# -----------------------------------------------
price = 100
discount = 20
print(f"Final price: {price - discount}")   # Output: 80

# -----------------------------------------------
# EXPRESSIONS inside { }
# -----------------------------------------------
name = "vinita"
print(f"Caps: {name.upper()}")              # Output: VINITA
print(f"Next year age: {age + 1}")          # Output: 22

# -----------------------------------------------
# DECIMAL FORMATTING
# -----------------------------------------------
cgpa = 7.0700
print(f"CGPA: {cgpa:.2f}")                 # Output: 7.07
# .2f means show only 2 decimal places

# -----------------------------------------------
# MULTIPLE VARIABLES in one f-string
# -----------------------------------------------
name = "Vinita"
age = 21
city = "Indore"
cgpa = 7.07
print(f"Hi! I am {name}, {age} years old from {city}. CGPA: {cgpa}")

# -----------------------------------------------
# MULTILINE f-string using \n
# -----------------------------------------------
print(f"Name: {name}\nAge: {age}\nCity: {city}")

# -----------------------------------------------
# QUICK SUMMARY
# -----------------------------------------------
# f"text {variable} text"   -> basic usage
# f"{a + b}"                -> math inside
# f"{name.upper()}"         -> method inside
# f"{cgpa:.2f}"             -> formatting decimals
# Everything inside ONE quote!



# VARIABLES & DATA TYPES — COMPLETE NOTES
# ========================================

# -----------------------------------------------
# WHAT IS A VARIABLE?
# -----------------------------------------------
# A variable is a box that stores a value
# Syntax: variable_name = value

name = "Vinita"      # stores text
age = 21             # stores number
cgpa = 7.07          # stores decimal
is_student = True    # stores True/False

# -----------------------------------------------
# VARIABLE NAMING RULES
# -----------------------------------------------
# ✅ Valid
my_name = "Vinita"
age1 = 21
_score = 100

# ❌ Invalid
# 1age = 21          # cannot start with number
# my-name = "hi"     # no hyphens allowed
# class = "DS"       # cannot use Python keywords

# -----------------------------------------------
# MULTIPLE ASSIGNMENT
# -----------------------------------------------
# Assign multiple values at once
name, age, city = "Vinita", 21, "Indore"

# Assign same value to multiple variables
x = y = z = 0

# -----------------------------------------------
# REASSIGNING VARIABLES
# -----------------------------------------------
x = 10
x = 20              # reassigned to new value
x = "hello"         # can even change type!

# -----------------------------------------------
# DATA TYPES
# -----------------------------------------------

# 1. int — whole numbers
age = 21
year = 2026
print(type(age))        # <class 'int'>

# 2. float — decimal numbers
cgpa = 7.07
price = 99.99
print(type(cgpa))       # <class 'float'>

# 3. str — text
name = "Vinita"
city = 'Indore'
print(type(name))       # <class 'str'>

# 4. bool — True or False only
is_student = True
has_job = False
print(type(is_student)) # <class 'bool'>
# Note: Capital T and F always!
# true = ❌ wrong
# True = ✅ correct

# 5. NoneType — empty / no value
result = None
print(type(result))     # <class 'NoneType'>

# -----------------------------------------------
# TYPE CONVERSION
# -----------------------------------------------
# str to int
age = int("21")         # "21" -> 21

# int to str
age = 21
print("Age: " + str(age))  # must convert to str

# int to float
x = float(5)            # 5 -> 5.0

# float to int — cuts decimal (not rounded!)
y = int(7.9)            # 7.9 -> 7

# str to float
price = float("99.99")  # "99.99" -> 99.99

# -----------------------------------------------
# CHECKING DATA TYPE
# -----------------------------------------------
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(cgpa))           # <class 'float'>
print(type(is_student))     # <class 'bool'>

# Check if specific type
print(isinstance(age, int))     # True
print(isinstance(name, int))    # False

# -----------------------------------------------
# DYNAMIC TYPING
# -----------------------------------------------
# Python variable type can change anytime!
x = 10              # int
x = "hello"         # now str
x = 3.14            # now float

# -----------------------------------------------
# QUICK SUMMARY
# -----------------------------------------------
# int      -> whole numbers     -> 21, 100, -5
# float    -> decimal numbers   -> 7.07, 99.99
# str      -> text              -> "Vinita", 'hello'
# bool     -> True or False     -> True, False
# NoneType -> empty value       -> None

name = "vinita"
print("my name is",name )

# mini challenge
name = "muskan"
print("info@datawith",name,".com", sep = "")
print("suppport@datawith",name,".com", sep="")#sep="" defines what character is placed between the items in print — by default it's a space, but you can change it to anything!



