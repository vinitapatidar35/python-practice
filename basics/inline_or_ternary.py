"""
inline_or_ternary.py

Covers:
- Ternary operator: variable = value_if_true if condition else value_if_false
- match-case statement with a wildcard (_) as default case
"""

mark = 95
marks = "you goT A my kiddo" if mark > 90 else "better luck next time"
print(marks)


country = "US"

match country:
    case "US":
        print("country is US")
    case "UK":
        print("country is UK")
    case "India":
        print("country is India")
    case _:
        print("not mention")