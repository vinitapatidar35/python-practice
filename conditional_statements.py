# ==============================================================================
# PYTHON CONDITIONAL STATEMENTS CHEAT SHEET
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE BASIC IF-ELIF-ELSE STRUCTURE
# ------------------------------------------------------------------------------
# Python relies on INDENTATION (usually 4 spaces) to define code blocks instead 
# of curly braces {} like other languages.

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:  # 'elif' is short for 'else if'
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:              # Triggers if none of the above conditions are met
    print("Grade: F")


# ------------------------------------------------------------------------------
# 2. NESTED CONDITIONALS
# ------------------------------------------------------------------------------
# You can put an 'if' statement inside another 'if' statement, though you 
# should use them sparingly to keep code readable.

has_ticket = True
is_vip = False

if has_ticket:
    if is_vip:
        print("Welcome to the VIP Lounge!")
    else:
        print("Welcome to the General Seats.")
else:
    print("Access Denied. Please purchase a ticket.")


# ------------------------------------------------------------------------------
# 3. THE TERNARY OPERATOR (Conditional Expression)
# ------------------------------------------------------------------------------
# A shortcut to write a simple if-else assignment on a single line.
# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


# ------------------------------------------------------------------------------
# 4. CONDITIONAL VALUES & "TRUTHY" vs "FALSY"
# ------------------------------------------------------------------------------
# You don't always need an explicit operator (like ==). Python evaluates 
# structural values directly as True or False in an 'if' statement.

# Falsy values: None, 0, "", [], {}, set(), False
# Truthy values: Everything else

cart = ["Laptop", "Mouse"]

if cart:  # Evaluates to True because the list is NOT empty
    print(f"Proceed to checkout with {len(cart)} items.")
else:
    print("Your cart is empty!")


# ------------------------------------------------------------------------------
# 5. STRUCTURAL PATTERN MATCHING (Match-Case)
# ------------------------------------------------------------------------------
# Available in Python 3.10+, this acts like a 'switch' statement found in 
# other languages and is ideal for matching specific values or patterns cleanly.

http_status = 404

match http_status:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 503:  # Using '|' acts as an 'or' operator inside patterns
        print("Server Error")
    case _:          # The underscore acts as a wildcard (catch-all) like 'else'
        print("Unknown Status Code")


# connecting condition using and , or

email = "vinitapatidar@66gmail.com"
#print("." in email and "@" in email )
if email == "" :
    print("email is empty")
elif "." not in email and "@" not in email:
    print("email contain . and @")
elif email.count("@") != 1:
    print("email contain exactly 1 @")
elif not email.endswith((".com",".org", ".net")):
    print("end with valid end point")
else:
    print("valid email")


email = "vinitapatidar66@gmail.com"


email = email.strip()

if email == "":
    print("Email cannot be empty.")

elif not ('.' in email and '@' in email):
    print("Email must contain . and @")

elif email.count('@') != 1:
    print("Email must contain exactly one @.")

elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")

elif len(email) > 254:
    print("Email must not be longer than 254 characters")

elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")

else:
    print("Email is valid.")