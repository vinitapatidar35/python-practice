import math

# --- 1. SCIENTIFIC CONSTANTS --------------------------------------------------
print(math.pi)   # 3.141592653589793  -> Circumference ratio (π)
print(math.e)    # 2.718281828459045  -> Natural growth/Euler base (e)
print(math.tau)  # 6.283185307179586  -> Full turn constant (τ = 2 * π)
print(math.inf)  # inf                -> Mathematical representation of infinity
print(math.nan)  # nan                -> Not a Number (missing/corrupted data)

# --- 2. ADVANCED ROUNDING & SIGNS --------------------------------------------
print(math.ceil(4.1))    #  5  (Forces float UP to next integer)
print(math.floor(4.9))   #  4  (Forces float DOWN to next integer)
print(math.trunc(7.99))  #  7  (Chops off decimals completely; same as int())
print(math.fabs(-12.3))  # 12.3 (Absolute value; always returns a positive float)

# --- 3. POWERS, ROOTS, & LOGARITHMS ------------------------------------------
print(math.sqrt(36))     # 6.0  (Square root calculator; returns float)
print(math.isqrt(37))    # 6    (Integer square root; truncates down to int)
print(math.pow(2, 3))    # 8.0  (Raises x to power of y; returns float)
print(math.log(100, 10)) # 2.0  (Logarithm with custom base. No base given = base 'e')
print(math.log2(8))      # 3.0  (Logarithm base 2 shortcut)
print(math.log10(1000))  # 3.0  (Logarithm base 10 shortcut)

# --- 4. NUMBER THEORY & BOOLEANS ---------------------------------------------
print(math.factorial(4)) # 24   (4 * 3 * 2 * 1)
print(math.gcd(18, 24))  # 6    (Greatest Common Divisor)
print(math.lcm(4, 6))    # 12   (Least Common Multiple)
# isclose() safely checks float equality by bypassing computer binary bugs:
print(math.isclose(0.1 + 0.2, 0.3)) # True (While 0.1 + 0.2 == 0.3 evaluates to False!)

# --- 5. TRIGONOMETRY (Expects RADIANS, not Degrees!) -------------------------
rad = math.radians(90)   # Converts 90° to ~1.57 radians (π / 2)
print(math.sin(rad))     # 1.0  (Sine function)
print(math.cos(rad))     # 0.0  (Cosine function; returns near-zero float format)
print(math.degrees(math.pi)) # 180.0 (Converts radians back to degrees)

# --- 6. CORE VS. MODULE EXTREMUMS (MIN / MAX) -------------------------------
# Core Built-ins: Work globally without imports on raw inputs or iterables (lists)
print(max(10, 20, 5), min([45.9, 12.5, 89.0])) # 20, 12.5

# Math Module Specialized: fmax() and fmin() safely ignore 'nan' data crashes
val1, val_nan = 14.5, math.nan
print(math.fmax(val1, val_nan)) # 14.5 (Safely filters out the nan)
print(math.fmin(val1, val_nan)) # 14.5 (Safely filters out the nan)

