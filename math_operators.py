# ==============================================================================
# MASTERING PYTHON MATHEMATICAL OPERATORS (FROM SCRATCH)
# ==============================================================================

# Let's set up two baseline variables to use for our examples
a = 15
b = 4

# ------------------------------------------------------------------------------
# 1. BASIC ARITHMETIC OPERATORS
# ------------------------------------------------------------------------------

# Addition (+)
total_sum = a + b
print(f"Addition (15 + 4): {total_sum}")          # Output: 19

# Subtraction (-)
difference = a - b
print(f"Subtraction (15 - 4): {difference}")      # Output: 11

# Multiplication (*)
product = a * b
print(f"Multiplication (15 * 4): {product}")      # Output: 60


# ------------------------------------------------------------------------------
# 2. THE TWO TYPES OF DIVISION (CRITICAL CONCEPT)
# ------------------------------------------------------------------------------

# True Division (/) -> ALWAYS returns a float (decimal), even if it divides evenly!
true_div = a / b
print(f"True Division (15 / 4): {true_div}")      # Output: 3.75
print(type(true_div))                             # <class 'float'>

# Floor Division (//) -> Chops off the decimal entirely, rounding DOWN to an integer.
floor_div = a // b
print(f"Floor Division (15 // 4): {floor_div}")  # Output: 3 (Since 4 goes into 15 three whole times)
print(type(floor_div))                            # <class 'int'>


# ------------------------------------------------------------------------------
# 3. MODULO (%) & EXPONENTIATION (**)
# ------------------------------------------------------------------------------

# Modulo (%) -> Returns ONLY the remainder left over after a division.
# Think: 15 divided by 4 is 3, with a remainder of 3 (4 * 3 = 12, and 15 - 12 = 3).
remainder = a % b
print(f"Modulo/Remainder (15 % 4): {remainder}")  # Output: 3

# Exponentiation (**) -> Raises a number to the power of another (a b)
power_result = a ** 2
print(f"Exponentiation (15 squared): {power_result}") # Output: 225


# ------------------------------------------------------------------------------
# 4. OPERATOR PRECEDENCE (PEMDAS / BODMAS)
# ------------------------------------------------------------------------------
# Just like algebra class, Python executes math operations in a strict order:
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication *, Division /, Floor Division //, Modulo % (Left to Right)
# 4. Addition +, Subtraction - (Left to Right)

calculation_1 = 5 + 3 * 2
print(f"No Parentheses (5 + 3 * 2): {calculation_1}")     # Output: 11 (Multiplication happens first!)

calculation_2 = (5 + 3) * 2
print(f"With Parentheses ((5 + 3) * 2): {calculation_2}") # Output: 16 (Parentheses happen first!)


# ------------------------------------------------------------------------------
# 5. SHORTCUT: AUGMENTED ASSIGNMENT OPERATORS
# ------------------------------------------------------------------------------
# If you want to update a variable using its own existing value, use these shortcuts:

score = 100

score += 5   # Equivalent to: score = score + 5
print(f"Updated Score (+5): {score}")            # Output: 105

score -= 10  # Equivalent to: score = score - 10
print(f"Updated Score (-10): {score}")           # Output: 95

score *= 2   # Equivalent to: score = score * 2
print(f"Updated Score (*2): {score}")            # Output: 190