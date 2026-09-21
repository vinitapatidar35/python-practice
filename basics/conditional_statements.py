"""
conditional_statements.py

Covers:
- if / elif / else structure (indentation-based blocks)
- Nested conditionals
- Ternary operator (conditional expression on one line)
- Truthy vs Falsy values in if conditions
- Structural pattern matching (match-case, Python 3.10+), including | for
  multiple matches and _ as wildcard
- Combining conditions with and / or / not
- A practical email-validation example using chained elif conditions
"""

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


has_ticket = True
is_vip = False

if has_ticket:
    if is_vip:
        print("Welcome to the VIP Lounge!")
    else:
        print("Welcome to the General Seats.")
else:
    print("Access Denied. Please purchase a ticket.")


age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


cart = ["Laptop", "Mouse"]

if cart:
    print(f"Proceed to checkout with {len(cart)} items.")
else:
    print("Your cart is empty!")


http_status = 404

match http_status:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 503:
        print("Server Error")
    case _:
        print("Unknown Status Code")


email = "vinitapatidar@66gmail.com"

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