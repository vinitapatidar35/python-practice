# ==============================================================================
# PYTHON BOOLEAN EXPRESSIONS CHEAT SHEET
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. VALUES
# ------------------------------------------------------------------------------
# Python's built-in boolean types. Note the capital letters!
t = True
f = False


# ------------------------------------------------------------------------------
# 2. FUNCTIONS
# ------------------------------------------------------------------------------
# bool(): Converts a value to a Boolean. 
# Empty collections ([], {}, ""), 0, and None evaluate to False. Everything else is True.
print(bool(0))          # Output: False
print(bool("Hello"))    # Output: True

# any(): Returns True if AT LEAST ONE element in an iterable is truthy.
print(any([False, True, False]))  # Output: True

# all(): Returns True ONLY if ALL elements in an iterable are truthy.
print(all([True, True, False]))   # Output: False

# isinstance(): Checks if an object is an instance of a specific class/type.
print(isinstance(5, int))         # Output: True


# ------------------------------------------------------------------------------
# 3. COMPARISON OPERATORS
# ------------------------------------------------------------------------------
# Used to compare two values; always evaluates to True or False.
a, b = 10, 5

print(a == b)  # False -> Equal to
print(a != b)  # True  -> Not equal to
print(a < b)   # False -> Less than
print(a > b)   # True  -> Greater than
print(a >= b)  # True  -> Greater than or equal to
print(a <= b)  # False -> Less than or equal to


# ------------------------------------------------------------------------------
# 4. LOGICAL OPERATORS
# ------------------------------------------------------------------------------
# Used to combine multiple conditional statements.
x, y = True, False

# and: Returns True if both statements are true
print(x and y)  # Output: False

# or: Returns True if at least one of the statements is true
print(x or y)   # Output: True

# not: Reverses the result (Returns False if the result is true)
print(not x)    # Output: False


# ------------------------------------------------------------------------------
# 5. MEMBERSHIP OPERATORS
# ------------------------------------------------------------------------------
# Used to test if a sequence/structure contains a specific item.
my_list = [1, 2, 3, 4, 5]

# in: Returns True if the sequence contains the specified value
print(3 in my_list)      # Output: True

# not in: Returns True if the sequence does NOT contain the specified value
print(10 not in my_list)  # Output: True


# ------------------------------------------------------------------------------
# 6. IDENTITY OPERATORS
# ------------------------------------------------------------------------------
# Used to check if two variables point to the exact same object in memory.
# Note: '==' checks if values are equal; 'is' checks if actual memory locations are identical.
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

# is: Returns True if both variables are the same object
print(list_a is list_b)  # True  (They point to the same memory slot)
print(list_a is list_c)  # False (Same values, but different objects in memory)

# is not: Returns True if both variables are not the same object
print(list_a is not list_c)  # Output: True


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



# ==============================================================================
# CONTROL MIXED CONDITIONS & OPERATOR PRECEDENCE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE GOLDEN RULE OF PRECEDENCE: "NOT, AND, OR"
# ------------------------------------------------------------------------------
# Python evaluates logical operators in a specific strict order:
#   1. not  (Highest priority)
#   2. and
#   3. or   (Lowest priority)

# Example without parentheses:
result = True or False and False
# How Python sees it: 'and' comes first -> False and False is False.
# Then it evaluates: True or False -> True.
print(result)  # Output: True


# ------------------------------------------------------------------------------
# 2. OVERRIDING WITH PARENTHESES ()
# ------------------------------------------------------------------------------
# Just like in math, parentheses force Python to evaluate an expression first.
# This makes your code readable and prevents logical bugs.

# Example with parentheses changing the behavior:
result_with_brackets = (True or False) and False
# Python evaluates the bracket first: (True or False) is True.
# Then it evaluates: True and False -> False.
print(result_with_brackets)  # Output: False


# ------------------------------------------------------------------------------
# 3. REAL-WORLD MIXED CONDITION PRACTICE
# ------------------------------------------------------------------------------
# Scenario: A user can access premium content if they are an admin, 
# OR if they have a subscription AND their account is active.

is_admin = False
has_subscription = True
is_active = False

# ❌ BAD PRACTICE (Confusing and error-prone):
# Even though 'and' takes priority naturally, it's hard to read at a glance.
can_access_bad = is_admin or has_subscription and is_active
print(can_access_bad)  # Output: False

#  GOOD PRACTICE (Explicit and safe):
# Grouping the related logic with parentheses leaves zero room for misinterpretation.
can_access_good = is_admin or (has_subscription and is_active)
print(can_access_good)  # Output: False


# ------------------------------------------------------------------------------
# 4. "SHORT-CIRCUIT" EVALUATION
# ------------------------------------------------------------------------------
# Python optimize mixed conditions using short-circuiting:
# - For 'and', if the first value is False, it skips evaluating the rest.
# - For 'or', if the first value is True, it skips evaluating the rest.

def check_heavy_database():
    print("Checking database...")  # Imagine this is a slow process
    return True

# Short-circuiting saves time here:
# Because 'is_admin' is True, Python completely ignores the database function!
is_admin = True
if is_admin or check_heavy_database():
    print("Access granted via short-circuit!")  # Database function never runs

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
