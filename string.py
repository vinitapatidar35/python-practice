# ==============================================================================
# PYTHON STRING DATA TYPE: COMPLETE REFERENCE NOTES
# ==============================================================================

# THE GOLDEN RULE OF STRINGS:
# Strings are IMMUTABLE. Once a string is created in memory, it CANNOT be altered.
# Any method that "modifies" a string actually returns a BRAND NEW string object.

# ------------------------------------------------------------------------------
# 1. THE IMMUTABILITY DEMONSTRATION (CRITICAL CONCEPT)
# ------------------------------------------------------------------------------
original_text = "iitm"
original_text.upper()  # You called the method, but didn't save the output!

print("1. Immutability Check:", original_text)  
# Output: "iitm" -> The real string DID NOT change!

# To actually update the variable, you must explicitly re-assign it:
original_text = original_text.upper()
print("2. After Re-assignment:", original_text)  
# Output: "IITM" -> Now the variable points to the new modified version.


# ------------------------------------------------------------------------------
# 2. CASE CONVERSION METHODS
# ------------------------------------------------------------------------------
sample = "learn PYTHON coding"

print(sample.upper())       # "LEARN PYTHON CODING" -> Converts all to uppercase
print(sample.lower())       # "learn python coding" -> Converts all to lowercase
print(sample.title())       # "Learn Python Coding" -> Capitalizes first letter of each word
print(sample.capitalize())  # "Learn python coding" -> Capitalizes ONLY the very first character
print(sample.swapcase())    # "LEARN python CODING" -> Inverts case of every character


# ------------------------------------------------------------------------------
# 3. CLEANUP & SUBSTRING REPLACEMENT
# ------------------------------------------------------------------------------
dirty_string = "   hello world   "

# Removing white spaces
print(dirty_string.strip())   # "hello world"  -> Removes spaces from BOTH ends
print(dirty_string.lstrip())  # "hello world   " -> Removes spaces ONLY from left
print(dirty_string.rstrip())  # "   hello world"  -> Removes spaces ONLY from right

# Replacing characters
msg = "apple bapple capple"
print(msg.replace("apple", "mango")) # "mango bmango cmango" -> Swaps all occurrences


# ------------------------------------------------------------------------------
# 4. SEARCHING, COUNTING & POSITION INDEXING
# ------------------------------------------------------------------------------
sentence = "python is fun and python is fast"

print(sentence.count("python"))  # Output: 2  -> Counts how many times it appears
print(sentence.find("is"))       # Output: 7  -> Returns lowest index where "is" starts
print(sentence.find("java"))     # Output: -1 -> Returns -1 if substring is NOT found

# .index() works exactly like .find(), but with one major difference:
print(sentence.index("is"))      # Output: 7
# print(sentence.index("java"))  # ERROR! Throws a ValueError if substring is missing


# ------------------------------------------------------------------------------
# 5. STRING VALIDATION METHODS (RETURNS True OR False)
# ------------------------------------------------------------------------------
val1 = "12345"
val2 = "Python"
val3 = "Python3"

print(val1.isdigit())  # True  -> Checks if ALL characters are numbers
print(val2.isalpha())  # True  -> Checks if ALL characters are letters
print(val3.isalnum())  # True  -> Checks if characters are alphanumeric (letters/numbers)

filename = "report.pdf"
print(filename.startswith("rep")) # True -> Verifies prefix
print(filename.endswith(".pdf"))   # True -> Verifies suffix


# ------------------------------------------------------------------------------
# 6. STRUCTURAL CONVERSION (SPLIT & JOIN)
# ------------------------------------------------------------------------------
# .split() converts a string into a LIST
data_string = "apple,banana,orange"
fruits_list = data_string.split(",") 
print(fruits_list)  # Output: ['apple', 'banana', 'orange']

# .join() converts a LIST back into a single string
hobbies = ["Coding", "Reading", "Gaming"]
joined_string = " - ".join(hobbies)
print(joined_string)  # Output: "Coding - Reading - Gaming"


# some practice

text = "   Hye i am BEAUTIFUL and KIND giRl   "
print(text.upper())
print(text.lower())
print(text.replace("KIND", "emotional"))
print(text.strip())
print(text.split(" "))

print("a" in text)
print(type(text))

age = 67
print("your age is : " + str(age))
print(type(age))
age = age + 10
age = str(age)
print(type(age))
print(age)

message = "hyee girl you are great in all the aspects"
print(message.count("e"))
print(len(message))
print("ha"*7)