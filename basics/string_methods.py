"""
string_methods.py

Covers:
- Function vs method (standalone function vs dot-notation method)
- Case modification: lower, upper, title, capitalize, swapcase
- Padding/alignment/stripping: strip, lstrip, rstrip, center, ljust, rjust, zfill
- Searching/counting: count, find, rfind, index, rindex
- Replacing/splitting: replace, split, rsplit, splitlines, partition, rpartition
- Joining lists into strings: join
- Boolean validation methods: isalnum, isalpha, isdigit, isnumeric, isdecimal,
  isidentifier, islower, isupper, istitle, isspace, isprintable
- Prefix/suffix checks: startswith, endswith, removeprefix, removesuffix
- Character translation: str.maketrans + translate
- Method chaining
- print() returns None - not to be used inside expressions/assignments
- Searching with find, index, count, startswith, endswith, and the 'in' operator
"""

x = "python"
print(len(x))

print(x.upper())


sample = "  hello Python 101!  "

print(sample.lower())
print(sample.upper())
print(sample.title())
print(sample.capitalize())
print(sample.swapcase())


text = "Python"
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.center(20, "-"))
print(text.ljust(20, "*"))
print(text.rjust(20, "*"))
print("42".zfill(5))


msg = "banana"
print(msg.count("a"))
print(msg.find("an"))
print(msg.rfind("an"))
print(msg.index("an"))
print(msg.rindex("an"))


csv_data = "apple,banana,cherry,dates"
print(csv_data.replace("banana", "orange"))
print(csv_data.split(","))
print(csv_data.split(",", 2))
print(csv_data.rsplit(",", 1))

multiline = "Line 1\nLine 2\rLine 3"
print(multiline.splitlines())

print("user@domain.com".partition("@"))
print("user@domain@com".rpartition("@"))


words = ["Python", "is", "awesome"]
print(" ".join(words))


print("Python123".isalnum())
print("Python".isalpha())
print("12345".isdigit())
print("12345".isnumeric())
print("12345".isdecimal())
print("my_var_1".isidentifier())
print("hello".islower())
print("HELLO".isupper())
print("Title Case".istitle())
print("   ".isspace())
print("Hello\n".isprintable())


filename = "script.py"
print(filename.startswith("sc"))
print(filename.endswith(".py"))
print("file.txt".removesuffix(".txt"))
print("test_file".removeprefix("test_"))


translation_table = str.maketrans("ae", "13")
print("apple tree".translate(translation_table))

# practice
text = " hello vinita "
print(text)
print(type(text))
print(len(text))
print(text.upper())
print(text.lower())
print(text.replace("hello", "hyee"))
print(text)
text = "hyee ,vinita"
print(text)
phone = "98-9876-4567"
print(phone.replace("-", ("")))
print(phone.replace("-", ("/")))

text = "  hello world  "
step1 = text.strip()
step2 = step1.replace(" ", "-")
final = step2.upper()

final = text.strip().replace(" ", "-").upper()
print(final)

phonee = "+49 (176) 123-4567"
print(phonee.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

txt = "my name is vinita and i am searching or preparing for internship."
print(txt.split(" "))

para = "     hyee      "
paraa = para.strip(" ")
print(paraa)
print(para.lstrip(" "))
print(para.rstrip(" "))
no_of_spaces = (len(para)) - (len(paraa))
print(no_of_spaces)


phrase = "Python is fun, Python is fast"

print(phrase.find("is"))
print(phrase.find("Java"))

print(phrase.index("is"))

print(phrase.count("Python"))

filename = "report.pdf"
print(filename.startswith("rep"))
print(filename.endswith(".csv"))

print("fun" in phrase)

phrase = "I Learn Python second time after a year later"
print(phrase.find("continue"))
print(phrase.index("time"))
print(phrase.startswith("I"))
print(phrase.endswith("bitch"))
print("time" in phrase)