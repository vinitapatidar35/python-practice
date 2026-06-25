# ==============================================================================
# PYTHON STRING INDEXING & SLICING CHEAT SHEET
# ==============================================================================

# Character Positions:
#  P   y   t   h   o   n     <- String
#  0   1   2   3   4   5     <- Positive Indexing (Left to Right)
# -6  -5  -4  -3  -2  -1     <- Negative Indexing (Right to Left)

text = "Python"

# ------------------------------------------------------------------------------
# 1. STRING INDEXING (Grabbing a single character)
# ------------------------------------------------------------------------------
# Syntax: string[index]

print(text[0])   # Positive Index: Grabs the very first character -> 'P'
print(text[3])   # Positive Index: Grabs the fourth character -> 'h'
print(text[-1])  # Negative Index: Grabs the last character -> 'n'
print(text[-3])  # Negative Index: Grabs the third character from the end -> 'h'

# ------------------------------------------------------------------------------
# 2. STRING SLICING (Extracting a chunk / substring)
# ------------------------------------------------------------------------------
# Syntax: string[start : stop]
# NOTE: 'start' index is INCLUDED, but 'stop' index is EXCLUDED (stops 1 before).

print(text[0:4])   # Slices from index 0 to 3 -> 'Pyth'
print(text[2:5])   # Slices from index 2 to 4 -> 'tho'
print(text[:3])    # Leaving 'start' empty defaults to the beginning -> 'Pyt'
print(text[2:])    # Leaving 'stop' empty goes all the way to the end -> 'thon'
print(text[-4:-1]) # Slicing using negative indexes -> 'tho'
print(text[:])     # Leaving both empty copies the entire string -> 'Python'

# ------------------------------------------------------------------------------
# 3. ADVANCED SLICING WITH STEP
# ------------------------------------------------------------------------------
# Syntax: string[start : stop : step]

numbers = "0123456789"

print(numbers[0:8:2]) # Slice from 0 to 7, skipping every 2nd character -> '0246'
print(numbers[::2])    # Skips every 2nd character across the whole string -> '02468'
print(numbers[1::2])   # Starts at index 1 and grabs all odd numbers -> '13579'

# ------------------------------------------------------------------------------
# 4. THE ULTIMATE REVERSAL TRICK
# ------------------------------------------------------------------------------
# Using a negative step (-1) tells Python to slice backward.

print(text[::-1])      # Reverses the string completely -> 'nohtyP'
print(numbers[::-2])   # Reverses the string and skips every 2nd number -> '97531'

txt = " i become an successful lady"
print(txt[1])
print(txt[-1])
print(txt[::-1])
print(txt[3:9])
print(txt[-1:-5:-1])
