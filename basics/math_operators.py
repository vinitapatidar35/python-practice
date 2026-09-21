"""
math_operators.py

Covers:
- Basic arithmetic operators: +, -, *
- True division (/) vs floor division (//)
- Modulo (%) and exponentiation (**)
- Operator precedence (PEMDAS/BODMAS)
- Augmented assignment operators (+=, -=, *=)
"""

a = 15
b = 4

total_sum = a + b
print(f"Addition (15 + 4): {total_sum}")

difference = a - b
print(f"Subtraction (15 - 4): {difference}")

product = a * b
print(f"Multiplication (15 * 4): {product}")


true_div = a / b
print(f"True Division (15 / 4): {true_div}")
print(type(true_div))

floor_div = a // b
print(f"Floor Division (15 // 4): {floor_div}")
print(type(floor_div))


remainder = a % b
print(f"Modulo/Remainder (15 % 4): {remainder}")

power_result = a ** 2
print(f"Exponentiation (15 squared): {power_result}")


calculation_1 = 5 + 3 * 2
print(f"No Parentheses (5 + 3 * 2): {calculation_1}")

calculation_2 = (5 + 3) * 2
print(f"With Parentheses ((5 + 3) * 2): {calculation_2}")


score = 100

score += 5
print(f"Updated Score (+5): {score}")

score -= 10
print(f"Updated Score (-10): {score}")

score *= 2
print(f"Updated Score (*2): {score}")