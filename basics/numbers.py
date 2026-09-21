"""
numbers.py

Covers:
- Numeric types: int, float, complex
- type() checking for numeric values
- Type casting between int/float/str, and truncation behavior
- complex() constructor to build complex numbers
- Operator overloading: * behaves differently for str vs int
- abs() - absolute value
- round() - rounding, including the "banker's rounding" .5 tie-break rule
  and rounding to specific decimal places
"""

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


distance_km = 5.64
print(type(distance_km))

steps_count = 8500
print(type(steps_count))

ac_signal = 12 - 5j
print(type(ac_signal))


points = int(distance_km)
print(type(points))

points = points + 20
print(points)


alert_code = "404"
print(type(alert_code))
print(alert_code * 3)

alert_code = int(alert_code)
print(type(alert_code))
print(alert_code * 3)


temperature = -4.75
print(int(temperature))
print(float(temperature))

horizontal_force = 15
vertical_force = 22
vector_result = complex(horizontal_force, vertical_force)
print(vector_result)


temperature_drop = -8
print(abs(temperature_drop))

coordinate_shift = -4.75
print(abs(coordinate_shift))


print(round(3.2))
print(round(3.8))

print(round(2.5))
print(round(3.5))

gas_price = 2.8764
print(round(gas_price, 2))
print(round(gas_price, 3))