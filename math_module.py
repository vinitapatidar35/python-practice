"""
math_module.py

Covers:
- Scientific constants: math.pi, math.e, math.tau, math.inf, math.nan
- Advanced rounding/signs: ceil, floor, trunc, fabs
- Powers, roots, logarithms: sqrt, isqrt, pow, log, log2, log10
- Number theory: factorial, gcd, lcm, isclose (safe float comparison)
- Trigonometry: radians, sin, cos, degrees
- Built-in max/min vs math module's nan-safe fmax/fmin
"""

import math

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

print(math.ceil(4.1))
print(math.floor(4.9))
print(math.trunc(7.99))
print(math.fabs(-12.3))

print(math.sqrt(36))
print(math.isqrt(37))
print(math.pow(2, 3))
print(math.log(100, 10))
print(math.log2(8))
print(math.log10(1000))

print(math.factorial(4))
print(math.gcd(18, 24))
print(math.lcm(4, 6))
print(math.isclose(0.1 + 0.2, 0.3))

rad = math.radians(90)
print(math.sin(rad))
print(math.cos(rad))
print(math.degrees(math.pi))

print(max(10, 20, 5), min([45.9, 12.5, 89.0]))

val1, val_nan = 14.5, math.nan
print(math.fmax(val1, val_nan))
print(math.fmin(val1, val_nan))