"""
string_indexing_slicing.py

Covers:
- Positive and negative indexing on strings
- String indexing: string[index]
- String slicing: string[start:stop] (start included, stop excluded)
- Slicing with step: string[start:stop:step]
- Reversing strings using a negative step
"""

text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-3])

print(text[0:4])
print(text[2:5])
print(text[:3])
print(text[2:])
print(text[-4:-1])
print(text[:])

numbers = "0123456789"

print(numbers[0:8:2])
print(numbers[::2])
print(numbers[1::2])

print(text[::-1])
print(numbers[::-2])

txt = " i become an successful lady"
print(txt[1])
print(txt[-1])
print(txt[::-1])
print(txt[3:9])
print(txt[-1:-5:-1]) 