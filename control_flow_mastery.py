"""
control_flow_mastery.py

Covers:
- Boolean values (True/False) and bool() conversion (truthy/falsy)
- any() and all() on iterables
- isinstance() type checking
- Comparison operators: ==, !=, <, >, >=, <=
- Logical operators: and, or, not
- Membership operators: in, not in
- Identity operators: is, is not (memory identity vs value equality)
- Operator precedence: not > and > or, and overriding with parentheses
- Real-world mixed conditions (readability with parentheses)
- Short-circuit evaluation for and/or
- Chained comparisons (e.g. 18 <= age <= 29)
- Practical validation examples combining bool(), len(), membership, isinstance()
"""

t = True
f = False

print(bool(0))
print(bool("Hello"))

print(any([False, True, False]))

print(all([True, True, False]))

print(isinstance(5, int))


a, b = 10, 5

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)


x, y = True, False

print(x and y)
print(x or y)
print(not x)


my_list = [1, 2, 3, 4, 5]

print(3 in my_list)
print(10 not in my_list)


list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b)
print(list_a is list_c)

print(list_a is not list_c)


email = "" 
name = "Vinita"
phone = ""

print(bool(any([email,name,phone])))
print(bool(all([email,name,phone])))

email = "@gmail.com" 
name = "Vinita"
phone = "678-09876-333"

print(bool(any([email,name,phone])))
print(bool(all([email,name,phone])))

email = "" 
name = ""
phone = ""

print(bool(any([email,name,phone])))
print(bool(all([email,name,phone])))


result = True or False and False
print(result)


result_with_brackets = (True or False) and False
print(result_with_brackets)


is_admin = False
has_subscription = True
is_active = False

can_access_bad = is_admin or has_subscription and is_active
print(can_access_bad)

can_access_good = is_admin or (has_subscription and is_active)
print(can_access_good)


def check_heavy_database():
    print("Checking database...")
    return True

is_admin = True
if is_admin or check_heavy_database():
    print("Access granted via short-circuit!")

x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)
z = x
print(x is z)

user_name = "Vinita"
age = 23
print(bool(user_name))
print(18 <= age <= 29)
task_1_passed = bool(user_name) and age >= 18
print(f"Task 1: {task_1_passed}")


password = "12345678"
task_2_passed = print(len(password)>=8 and " " not in password)
print(f"Task 2: {task_2_passed}")  

email = "vinitapatidar@gmail.com"
task_3_passed = bool(email) and "@" in email and email.endswith(".com")
print(f"Task 3: {task_3_passed}")  

username = "Vinita"
task_4_passed = username is not None and isinstance(username, str) and len(username) > 5
print(f"Task 4: {task_4_passed}")