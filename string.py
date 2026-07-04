"""
string.py

Covers:
- String immutability (methods return new strings, originals unchanged)
- Case conversion: upper, lower, title, capitalize, swapcase
- Cleanup: strip, lstrip, rstrip
- Substring replacement: replace
- Searching/counting: count, find, index
- Validation methods: isdigit, isalpha, isalnum, startswith, endswith
- Structural conversion: split, join
- Membership check with 'in', type(), string-int conversion, string repetition
"""

original_text = "iitm"
original_text.upper()

print("1. Immutability Check:", original_text)

original_text = original_text.upper()
print("2. After Re-assignment:", original_text)


sample = "learn PYTHON coding"

print(sample.upper())
print(sample.lower())
print(sample.title())
print(sample.capitalize())
print(sample.swapcase())


dirty_string = "   hello world   "

print(dirty_string.strip())
print(dirty_string.lstrip())
print(dirty_string.rstrip())

msg = "apple bapple capple"
print(msg.replace("apple", "mango"))


sentence = "python is fun and python is fast"

print(sentence.count("python"))
print(sentence.find("is"))
print(sentence.find("java"))

print(sentence.index("is"))


val1 = "12345"
val2 = "Python"
val3 = "Python3"

print(val1.isdigit())
print(val2.isalpha())
print(val3.isalnum())

filename = "report.pdf"
print(filename.startswith("rep"))
print(filename.endswith(".pdf"))


data_string = "apple,banana,orange"
fruits_list = data_string.split(",")
print(fruits_list)

hobbies = ["Coding", "Reading", "Gaming"]
joined_string = " - ".join(hobbies)
print(joined_string)


text = "   Hye i am BEAUTIFUL and KIND giRl   "
print(text.upper())
print(text.lower())
print(text.replace("KIND", "emotional"))
print(text.strip())
print(text.split(" "))

print("a" in text)
print(type(text))

age = 67
print("your age is : " + str(age))
print(type(age))
age = age + 10
age = str(age)
print(type(age))
print(age)

message = "hyee girl you are great in all the aspects"
print(message.count("e"))
print(len(message))
print("ha"*7)

