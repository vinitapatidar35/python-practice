# ==============================================================================
# MASTER COGNITIVE STUDY GUIDE: PYTHON LOOPS & ITERATION ARCHITECTURE
# ==============================================================================
# 💡 OVERVIEW:
#   Loops are control structures used to repeat a block of code execution.
#   - FOR LOOPS: Used for Definite Iteration (running a known number of times).
#   - WHILE LOOPS: Used for Indefinite Iteration (running until a condition changes).
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: THE FOR LOOP (SEQUENCE ITERATOR)
# ------------------------------------------------------------------------------
# 📝 SYNTAX SCHEMA:
#   for element in iterable_sequence:
#       # Code block to repeat for each element

print("--- Section 1A: Iterating Over a List Collection ---")
grocery_list = ["eggs", "milk", "bread"]

for item in grocery_list:
    print(f"Pipeline processing inventory item: {item}")


print("\n--- Section 1B: Iterating Over a String Sequence ---")
word = "CODE"

for letter in word:
    print(f"Extracting character slice: {letter}")


# ------------------------------------------------------------------------------
# SECTION 2: THE RANGE() ENGINE FOR NUMERIC LOOPS
# ------------------------------------------------------------------------------
# 📝 SYNTAX SCHEMA:
#   range(stop) -> Counts from 0 up to (but excluding) stop.
#   range(start, stop) -> Counts from start up to (but excluding) stop.
#   range(start, stop, step) -> Counts incrementing/decrementing by step amount.



print("\n--- Section 2A: range(stop) ---")
for i in range(3):
    print(f"Default zero-indexed step count: {i}") # Prints 0, 1, 2

print("\n--- Section 2B: range(start, stop) ---")
for i in range(5, 8):
    print(f"Bounded range step count: {i}") # Prints 5, 6, 7

print("\n--- Section 2C: range(start, stop, step) ---")
for i in range(10, 21, 5):
    print(f"Stepped range count: {i}") # Prints 10, 15, 20


# ------------------------------------------------------------------------------
# SECTION 3: THE WHILE LOOP (CONDITIONAL TESTER)
# ------------------------------------------------------------------------------
# 📝 SYNTAX SCHEMA:
#   while conditional_expression_is_true:
#       # Code block to execute
#       # State modifier (Crucial to prevent infinite execution loops!)



print("\n--- Section 3: While Loop Lifecycles ---")
battery_power = 3

while battery_power > 0:
    print(f"Device running. Remaining charge: {battery_power}%")
    # State modifier: decrementing keeps the script from running forever
    battery_power -= 1 

print("System Alert: Battery dead. Shutdown complete.")


# ------------------------------------------------------------------------------
# SECTION 4: LOOP CONTROL MODIFIERS (break, continue, else)
# ------------------------------------------------------------------------------
# These special inside-gate expressions instantly alter the loop tracking state.

print("\n--- Section 4A: The 'break' Statement ---")
# break: Instantly aborts the loop container entirely.
for score in range(1, 10):
    if score == 4:
        print("Target threshold hit! Emergency break triggered.")
        break
    print(f"Score registered: {score}")


print("\n--- Section 4B: The 'continue' Statement ---")
# continue: Skips the remainder of the current step loop, jumps to next item check.
for floor in range(1, 6):
    if floor == 3:
        print("Floor 3 under construction. Skipping!")
        continue
    print(f"Elevator opening at floor: {floor}")


print("\n--- Section 4C: The Loop 'else' Block ---")
# else: Runs ONLY if the loop finishes its sequence completely without hitting a 'break'.
search_target = "admin_access"
permissions = ["guest_view", "user_edit", "moderator_delete"]

for permission in permissions:
    if permission == search_target:
        print("Access Granted!")
        break
else:
    print(f"Security Alert: '{search_target}' not found anywhere in list.")


# ------------------------------------------------------------------------------
# SECTION 5: PRACTICAL PRODUCTION APPLICATION (EMAIL PIPELINE BULK CHECK)
# ------------------------------------------------------------------------------
print("\n--- Section 5: Real-World Batch Processing Pipeline ---")

incoming_batch = ["user1@gmail.com", "bad_email_no_at.com", "admin@org.net"]

for email_to_test in incoming_batch:
    # Reusing the validation logic from your coursework screenshot pipeline:
    if not ('@' in email_to_test and '.' in email_to_test):
        print(f"❌ REJECTED: '{email_to_test}' failed basic symbol integrity.")
        continue # Skip processing this bad email, go directly to the next one!
        
    print(f"✅ APPROVED: '{email_to_test}' successfully queued for dispatch.")

i = 1
for i in range(6):
    print(f"ROUND : {i}")
    i = i + 1

items = (1,2,3,4,5,6,7)
for item in items:
    print(f"i have {item} chocolate")

name = "Vinita"
for letter in name:
    print(letter, end = " ")

#ep (Separator): Controls the spacing inside a single print line by changing the character inserted between multiple objects separated by commas.
#end (Line-Ender): Controls the spacing outside the print line by changing what gets appended at the very tail end of a print statement execution (by default, a newline).

scores = [80,90,99,87,76]
sum = 0
for score in scores:
    sum = sum + score
print("\n", sum)

files = ["datA.csv " , " file.txt  " , "endinG.TXT"]
for file in files:
    x = file.strip().lower().replace("csv", "txt")
    print(x)

for x in range(11):
    print(f"7 * {x} = {7 * x}")

for x in range(6):
    print("*" * x)

row = 6
for x in range(1 , row +1):
    spaces = " "  * (row - x)
    star = "*" * x
    print(f"{spaces}{star}")

#   - break:    Instantly kills the loop entirely.
#   - continue: Skips the rest of the current loop cycle and goes to the next one.
#   - pass:     A silent, blank placeholder that does nothing (stops syntax errors).

names = ['maria', "arena" ," " ,"luca" , "messi" ]
for name in names:
    if name == " ":
        pass
    else:
        print(name)

for name in names:
    if name == "luca":
        continue
    else:
        print(name)    

for name in names:
    if name == "arena":
        break
    else:
        print(name)


week_days = ["Mon", "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]

for week_day in week_days:
    if week_days == "Mon" or "Tue" or "Wed" or "Thu" or "Fri":
        print("hurreee working days: " + week_days)
    else:
        pass