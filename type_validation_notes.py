"""
type_validation_notes.py

Covers:
- isinstance(variable, type) - structural type checking
- isinstance() with a tuple of types
- float.is_integer() - checks if a float's value has no fractional part
- Combining isinstance() and is_integer() as a validation pipeline
"""

x = 5.0

print(isinstance(x, float))
print(isinstance(x, int))

print(x.is_integer())

y = 5.5
print(y.is_integer())


user_input = 12.0

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