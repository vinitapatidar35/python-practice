# ==============================================================================
# STUDY NOTES: DATA VALIDATION (isinstance vs. is_integer)
# ==============================================================================
# 💡 OVERVIEW: 
#   Validation means checking data integrity before processing it to prevent 
#   bugs, logical errors, or application crashes.

# ------------------------------------------------------------------------------
# 1. isinstance(variable, type) -> THE STRUCTURAL TYPE CHECK
# ------------------------------------------------------------------------------
#   - Purpose: Checks if a variable belongs to a specific datatype box.
#   - Focuses on: Structural data type (how it is saved in memory).
#   - Returns: True / False.

x = 5.0

print(isinstance(x, float))  # Output: True  (It is stored as a float)
print(isinstance(x, int))    # Output: False (It does not have an int type label)


# ------------------------------------------------------------------------------
# 2. float.is_integer() -> THE NUMERIC VALUE CHECK
# ------------------------------------------------------------------------------
#   - Purpose: Checks if a decimal number has an empty fractional part (.0).
#   - Focuses on: Mathematical numerical value, NOT the type box.
#   - Returns: True / False.
#   - ⚠️ CRITICAL WARNING: Can ONLY be used on floats. Calling on an 'int' crashes.

print(x.is_integer())        # Output: True  (Value is 5.0 -> remainder is zero)

y = 5.5
print(y.is_integer())        # Output: False (Value is 5.5 -> remainder is .5)


# ------------------------------------------------------------------------------
# 3. PRODUCTION BEST PRACTICE: THE PIPELINE
# ------------------------------------------------------------------------------
# Combines both tools to safely inspect data from an external source without crashing.

user_input = 12.0

# Rule: Check structural type FIRST, then safely inspect value remainder SECOND.
if isinstance(user_input, float) and user_input.is_integer():
    clean_data = int(user_input)
    print(f"Validation Passed! Safe whole number: {clean_data}")
else:
    print("Validation Failed: Data contains active fraction remainders or wrong type.")

dat = 75
print(isinstance(dat,int))

data = 99.9
print(isinstance(data, (float , int)))

num = 45
print(num.is_integer())

# ==============================================================================
# SUMMARY: THE TWO GOLDEN RULES OF NUMERIC VALIDATION
# ==============================================================================

# RULE 1: STRUCTURAL LABELS (isinstance)
# Use it when you care about the storage TYPE.
# isinstance(5.0, int) -> False (Because it's a float box)

# RULE 2: MATHEMATICAL VALUES (.is_integer())
# Use it when you care about the VALUE inside a float box.
# 5.0.is_integer()    -> True  (Because mathematically, it's a whole number!)
#is_integer is a method which check is the number is whole number perfectly or not