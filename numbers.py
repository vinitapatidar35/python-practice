marks = 98.7
print(type(marks))
cgpa = 9
print(type(cgpa))
complex_stuff = 3 + 4j
print(type(complex_stuff))

marks = int(marks)
print(type(marks))
marks = marks - 12
print(marks)

x = "78"
print(type(x))
print(x * 3)
x = int(x)
print(type(x))
print(x * 3)


x = 3.14
print(int(x))
print(float(x))

a = 2
b = 6
print(complex(a,b))

# ==============================================================================
# FRESH STUDY NOTES: NUMERIC DATA TYPES, TYPE CASTING, & OPERATOR BEHAVIOR
# ==============================================================================

# ------------------------------------------------------------------------------
# TOPIC 1: PYTHON'S CORE NUMERIC DATA TYPES
# ------------------------------------------------------------------------------
# CONCEPT: Python automatically determines the data type based on how you write
# the value. It tracks these using built-in classes.
# SYNTAX: type(variable_name) -> Returns the data type class of the variable.

distance_km = 5.64
print(type(distance_km))    # <class 'float'>   -> Numbers with decimal points.

steps_count = 8500
print(type(steps_count))    # <class 'int'>     -> Whole numbers (no decimals).

ac_signal = 12 - 5j
print(type(ac_signal))      # <class 'complex'> -> Numbers with real (12) and imaginary (-5j) parts.


# ------------------------------------------------------------------------------
# TOPIC 2: EXPLICIT TYPE CASTING & TRUNCATION
# ------------------------------------------------------------------------------
# CONCEPT: Type casting is manually converting a value from one data type to another.
# WARNING (TRUNCATION): Converting a float to an int does NOT round the number. 
# It completely drops (chops off) the decimal part.

# Imagine calculating reward points where you only get points for whole kilometers completed
points = int(distance_km)   # Converts 5.64 to 5 (drops the .64 entirely)
print(type(points))         # <class 'int'>

points = points + 20        # Standard integer arithmetic: 5 + 20
print(points)               # Output: 25


# ------------------------------------------------------------------------------
# TOPIC 3: OPERATOR OVERLOADING (* OPERATOR CONTEXT)
# ------------------------------------------------------------------------------
# CONCEPT: The multiplication operator (*) changes its behavior completely 
# depending on the data type of the variables it is interacting with.
#
# Context A: String * Integer  -> Acts as REPLICATION (repeats text sequence).
# Context B: Integer * Integer -> Acts as MATHEMATICAL MULTIPLICATION.

alert_code = "404"
print(type(alert_code))     # <class 'str'> (Text data)
print(alert_code * 3)       # Output: '404404404' (Repeats the characters "404" three times)

alert_code = int(alert_code) # Type casting: Converts string text "404" to actual integer 404
print(type(alert_code))     # <class 'int'>
print(alert_code * 3)       # Output: 1212 (Performs actual mathematical math: 404 * 3)


# ------------------------------------------------------------------------------
# TOPIC 4: CONVERSIONS & COMPLEX NUMBER CONSTRUCTORS
# ------------------------------------------------------------------------------
# CONCEPT: You can freely cast numbers or combine individual integers to manufacture 
# a complex number dynamically.
# SYNTAX: complex(real_value, imaginary_value)

temperature = -4.75
print(int(temperature))     # Output: -4 (Truncates decimal toward zero)
print(float(temperature))   # Output: -4.75 (Keeps floating-point structure)

horizontal_force = 15
vertical_force = 22
# Pass two numbers into complex(): first becomes real, second becomes imaginary
vector_result = complex(horizontal_force, vertical_force)
print(vector_result)        # Output: (15+22j)


#----------------------------------------------------------------------------------------------------------------------

# ==============================================================================
# STUDY NOTES: CORE BUILT-IN FUNCTIONS - abs() & round()
# ==============================================================================

# ------------------------------------------------------------------------------
# TOPIC 1: abs(x) — THE ABSOLUTE VALUE
# ------------------------------------------------------------------------------
# 💡 THEORY:
#   - Absolute value represents the DISTANCE of a number from zero on a number line.
#   - Distance can never be negative, so abs() simply strips away the minus sign.
#   - MECHANICS: Positive numbers stay positive, negative numbers become positive.
#   - DATA TYPE RULE: It preserves the exact input type (int stays int, float stays float).

temperature_drop = -8
print(abs(temperature_drop))  # Output: 8 (<class 'int'>)

coordinate_shift = -4.75
print(abs(coordinate_shift))  # Output: 4.75 (<class 'float'>)


# ------------------------------------------------------------------------------
# TOPIC 2: round(number, ndigits) — THE NEAREST APPROXIMATION
# ------------------------------------------------------------------------------
# 💡 THEORY:
#   - Changes a decimal number to its nearest whole number or specific decimal place.
#   - SYNTAX: round(number) or round(number, decimal_places)
#
#   - ⚠️ THE CRITICAL ".5 TRAP" (BANKER'S ROUNDING):
#     If a number falls EXACTLY halfway between two integers (ends in .5), Python
#     does NOT always round up. It rounds to the nearest EVEN number!
#     Why? To eliminate statistical bias when calculating averages in big data.

# Case A: Standard behavior (Closer to one side)
print(round(3.2))        # Output: 3  (3.2 is closer to 3)
print(round(3.8))        # Output: 4  (3.8 is closer to 4)

# Case B: Tie-Breaker behavior (Ends exactly in .5 -> Moves to nearest EVEN number)
print(round(2.5))        # Output: 2  (2 is even, so it rounds DOWN)
print(round(3.5))        # Output: 4  (4 is even, so it rounds UP)

# Case C: Decimal precision handling (Using the 2nd argument)
gas_price = 2.8764
print(round(gas_price, 2))  # Output: 2.88 (Checks the 3rd digit '6', rounds up)
print(round(gas_price, 3))  # Output: 2.876 (Checks the 4th digit '4', rounds down)

