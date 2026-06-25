# ==============================================================================
# FUNCTIONS vs METHODS (Ultra-Short)
# ==============================================================================

# FUNCTION: Independent. You pass data INSIDE it.
# Syntax: function(data)

x = "python"
print(len(x))      # len() is a standalone function


# METHOD: Dependent. Attached to a specific type via a DOT (.).
# Syntax: data.method()

print(x.upper())   # .upper() is a method belonging ONLY to strings




# ==============================================================================
# THE ULTIMATE PYTHON STRING METHODS CHEAT SHEET
# ==============================================================================

sample = "  hello Python 101!  "

# ------------------------------------------------------------------------------
# 1. CASE MODIFICATIONS
# ------------------------------------------------------------------------------
print(sample.lower())        # Converts all characters to lowercase -> "  hello python 101!  "
print(sample.upper())        # Converts all characters to uppercase -> "  HELLO PYTHON 101!  "
print(sample.title())        # Capitalizes first letter of every word -> "  Hello Python 101!  "
print(sample.capitalize())   # Capitalizes ONLY the first character of the whole string -> "  hello python 101!  "
print(sample.swapcase())     # Inverts lowercase to uppercase and vice versa -> "  HELLO pYTHON 101!  "

# ------------------------------------------------------------------------------
# 2. PADDING, ALIGNMENT & STRIPPING
# ------------------------------------------------------------------------------
text = "Python"
print(text.strip())          # Removes leading and trailing whitespaces
print(text.lstrip())         # Removes leading (left) whitespaces
print(text.rstrip())         # Removes trailing (right) whitespaces
print(text.center(20, "-"))  # Centers string within width, padded with char -> "-------Python-------"
print(text.ljust(20, "*"))   # Left-aligns string within width, padded -> "Python**************"
print(text.rjust(20, "*"))   # Right-aligns string within width, padded -> "**************Python"
print("42".zfill(5))         # Pads number string with leading zeros -> "00042"

# ------------------------------------------------------------------------------
# 3. SEARCHING & COUNTING
# ------------------------------------------------------------------------------
msg = "banana"
print(msg.count("a"))        # Counts occurrences of a substring -> 3
print(msg.find("an"))        # Returns lowest index of substring (returns -1 if not found) -> 1
print(msg.rfind("an"))       # Returns highest (rightmost) index of substring -> 3
print(msg.index("an"))       # Like find(), but raises ValueError if not found -> 1
print(msg.rindex("an"))      # Like rfind(), but raises ValueError if not found -> 3

# ------------------------------------------------------------------------------
# 4. REPLACING & SPLITTING
# ------------------------------------------------------------------------------
csv_data = "apple,banana,cherry,dates"
print(csv_data.replace("banana", "orange")) # Replaces old substring with new -> "apple,orange,cherry,dates"
print(csv_data.split(","))                  # Splits string into a list by delimiter -> ['apple', 'banana', 'cherry', 'dates']
print(csv_data.split(",", 2))               # Splits from left, max splits = 2 -> ['apple', 'banana', 'cherry,dates']
print(csv_data.rsplit(",", 1))              # Splits from right, max splits = 1 -> ['apple,banana,cherry', 'dates']

multiline = "Line 1\nLine 2\rLine 3"
print(multiline.splitlines())               # Splits string at line breaks -> ['Line 1', 'Line 2', 'Line 3']

# Partition splits at the FIRST match and returns a 3-tuple: (before, match, after)
print("user@domain.com".partition("@"))     # -> ('user', '@', 'domain.com')
print("user@domain@com".rpartition("@"))    # Splits at LAST match -> ('user@domain', '@', 'com')

# ------------------------------------------------------------------------------
# 5. JOINING LISTS
# ------------------------------------------------------------------------------
words = ["Python", "is", "awesome"]
print(" ".join(words))       # Joins items of an iterable using the string as separator -> "Python is awesome"

# ------------------------------------------------------------------------------
# 6. BOOLEAN CHECKS & VALIDATION (Returns True or False)
# ------------------------------------------------------------------------------
print("Python123".isalnum()) # True if all characters are alphanumeric (letters/numbers)
print("Python".isalpha())    # True if all characters are letters
print("12345".isdigit())     # True if all characters are digits
print("12345".isnumeric())   # True if characters are numeric (includes fractions/roman numerals)
print("12345".isdecimal())   # True if characters are strict decimals (base 10 numbers)
print("my_var_1".isidentifier()) # True if string is a valid Python variable/identifier name
print("hello".islower())     # True if all cased characters are lowercase
print("HELLO".isupper())     # True if all cased characters are uppercase
print("Title Case".istitle())# True if string follows title case rules
print("   ".isspace())       # True if string contains only whitespace characters
print("Hello\n".isprintable()) # False if it contains invisible chars like newlines/tabs

# ------------------------------------------------------------------------------
# 7. PREFIX & SUFFIX CHECKS
# ------------------------------------------------------------------------------
filename = "script.py"
print(filename.startswith("sc")) # True if string starts with specified prefix
print(filename.endswith(".py"))   # True if string ends with specified suffix
print("file.txt".removesuffix(".txt")) # Removes the suffix if present -> "file"
print("test_file".removeprefix("test_")) # Removes the prefix if present -> "file"

# ------------------------------------------------------------------------------
# 8. ADVANCED CHARACTER TRANSLATION
# ------------------------------------------------------------------------------
# maketrans creates a mapping table, translate applies it
# This example swaps 'a' with '1' and 'e' with '3'
translation_table = str.maketrans("ae", "13")
print("apple tree".translate(translation_table)) # -> "1ppl3 tr33"

#practice
text =" hello vinita "
print(text)
print(type(text))
print(len(text))
print(text.upper())
print(text.lower())
print(text.replace("hello" , "hyee"))
print(text)
text = "hyee ,vinita"
print(text)
phone = "98-9876-4567"
print(phone.replace("-", ("")))
print(phone.replace("-", ("/")))

#Method chaining is a technique where you call multiple methods one after another in a single line of code. It works like an 
# assembly line: each method performs an action on the data and passes the result directly to the next method from left to right.

text = "  hello world  "

# Without chaining (creates messy intermediate variables)
step1 = text.strip()          # "hello world"
step2 = step1.replace(" ", "-") # "hello-world"
final = step2.upper()         # "HELLO-WORLD"

# With chaining (clean and concise)
final = text.strip().replace(" ", "-").upper()
print(final)  # Output: "HELLO-WORLD"

phonee = "+49 (176) 123-4567"
print(phonee.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ",""))

txt = "my name is vinita and i am searching or preparing for internship."
print(txt.split(" "))

para = "     hyee      "
paraa = para.strip(" ")
print(paraa)
print(para.lstrip(" "))
print(para.rstrip(" "))
no_of_spaces = (len(para)) - (len(paraa))
print(no_of_spaces)

# LESSON: print() only displays text; it returns None.
# Never use print() inside math equations or variable assignments!

# ==============================================================================
# PYTHON STRING SEARCHING METHODS
# ==============================================================================

phrase = "Python is fun, Python is fast"

# 1. .find(substring) -> Returns the first index where it's found (or -1 if missing)
print(phrase.find("is"))       # Output: 7 (index of the first 'is')
print(phrase.find("Java"))     # Output: -1 (does not exist, no error thrown)

# 2. .index(substring) -> Same as find(), but crashes if missing
print(phrase.index("is"))      # Output: 7
# print(phrase.index("Java"))  # ❌ Throws a ValueError! Use with caution.

# 3. .count(substring) -> Counts how many times it appears
print(phrase.count("Python"))  # Output: 2

# 4. .startswith(substring) & .endswith(substring) -> Returns True or False
filename = "report.pdf"
print(filename.startswith("rep")) # Output: True
print(filename.endswith(".csv"))   # Output: False

# 5. The 'in' operator -> The easiest way to check if a word is present
print("fun" in phrase)         # Output: True

phrase = "I Learn Python second time after a year later"
print(phrase.find("continue"))
print(phrase.index("time"))
print(phrase.startswith("I"))
print(phrase.endswith("bitch"))
print("time" in phrase)