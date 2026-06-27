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
    if week_day == "Mon" or week_day == "Tue" or week_day == "Wed" or week_day == "Thu" or week_day == "Fri":
        print("hurreee working days: " + week_day)
    else:
        pass

list = [1,2,3]
for item in list:
    print(f"{item}")
else:
    print("no item ")


names = ["maria", "arena", "luca", "messi"]

print("--- Scenario 1: Searching for a name that EXISTS ---")
for name in names:
    if name == "luca":
        print("Found luca! Breaking out of loop.")
        break  # Triggers a break -> skips the else block completely!
else:
    print("Alert: The target name was not found in the list.")


print("\n--- Scenario 2: Searching for a name that DOES NOT exist ---")
for name in names:
    if name == "vinita":
        print("Found vinita! Breaking out of loop.")
        break
else:
    # This runs because the loop checked everyone and never hit 'break'
    print("Alert: 'vinita' was not found in the list.")


names = ["alifia", "saddow" , "bunna" ,None,"brozza"]
for name in names:
    if name == None:
        print("Error in Data , missing value ")
        break
else:
    print("no missing anme , everything is right in data.")

Files = ["data.csv", "study.csv" , "school.csv", "student.txt"]
for file in Files:
    if file.endswith(".txt"):
        x = file.replace(".txt",".csv")
        print(x)
    else:
        print(file)
else:
    print("all files are csv files.")

Files = ["data.csv", "study.csv" , "school.csv", "student.txt"]
for file in Files:
    if file.endswith(".txt"):
        print("unnecessary file")
        break 
else:
    print("clean required file")

files = ["data.csv", "study.csv" , "school.csv", "student.txt",  "school.csv", "student.txt"]
seen_files = []
for file in files:
    if file in seen_files:
        print("found duplicate")
        break
    else:
        seen_files.append(file)
else:
    print("all are unique file")
    

# ==============================================================================
# DEFINITIONS: NESTED LOOP vs. NESTED FOR LOOP
# ==============================================================================

# 💡 NESTED LOOP DEFINITION:
# A generic programming control flow structure where any loop statement 
# (which can be a 'for' loop or a 'while' loop) is placed entirely inside the 
# body of another loop statement. The inner loop executes its complete cycle 
# of iterations for every single individual iteration of the outer loop.

# 💡 NESTED FOR LOOP DEFINITION:
# A specific type of nested loop where a definite 'for' loop is placed inside 
# another 'for' loop. It is primarily used to iterate over multi-dimensional 
# data structures (like matrices or grids) or combinations of sequences, where 
# the outer 'for' loop tracks the primary sequence and the inner 'for' loop 
# completely exhausts its sequence on every single step of the outer tracker.

for x in range(3):
    for y in range(2):
        print(f"{x * y}")
        print(f"{x},{y}")
        print("\n") 

colors = ["red" , "blue" , "green" , "golden" , "silver"]
tshirts = ["one", "two"]
count = 0

for color in colors:
    for tshirt in tshirts:
        print(f"count total number of combination {color}, {tshirt} {count} combination")
        count = count + 1
print(f"total number of combination {count}")

# ==============================================================================
# DIAGRAM ARCHITECTURE ANALYSIS: TRIPLE-NESTED LOOPS (3-LEVEL HIERARCHIES)
# Reference File: image_545fa2.jpg
# ==============================================================================

# 💡 VISUAL CONCEPT OVERVIEW:
# The diagram in image_545fa2.jpg illustrates how deeply nested loops process 
# hierarchical, tree-structured data across three distinct real-world use cases. 
# For every single step in an outer level loop, the inner child loops must fully 
# exhaust their entire cycle from left to right.

# ------------------------------------------------------------------------------
# USE CASE 1: TIME-SERIES CHRONOLOGICAL PIPELINE (Top-Left Tree Structure)
# ------------------------------------------------------------------------------
# Hierarchical levels broken down visually:
#   - Level 1 (Slowest): Iterates through years (e.g., 2026, 2027)
#   - Level 2 (Medium):  Branches out into months for that year (Jan, Feb, Mar)
#   - Level 3 (Fastest): Iterates through individual days within that month (1, 2, 3)

for year in years:                     # Level 1: Focuses on one year at a time
    for month in months:               # Level 2: Fully cycles through all months of that year
        for day in days:  
            pass             # Level 3: Runs for every single day of that month
            # Do Something (Action)    # Target: Fired individually for every unique calendar date


# ------------------------------------------------------------------------------
# USE CASE 2: RELATIONAL DATABASE MATRIX EXTRACTION (Right-Side Table Structure)
# ------------------------------------------------------------------------------
# Hierarchical levels broken down visually:
#   - Level 1 (Slowest): Selects a distinct Database Table from a collection
#   - Level 2 (Medium):  Targets individual vertical Columns within that selected Table
#   - Level 3 (Fastest): Steps horizontally through each specific Row cell block inside that Column

for table in tables:                   # Level 1: Selects Table A, then Table B
    for col in columns:                # Level 2: Steps through Column 1, 2, 3...
        for row in rows:  
            pass             # Level 3: Accesses individual cell rows within the column
            # Do Something             # Target: Performs data extraction per cell intersection


# ------------------------------------------------------------------------------
# USE CASE 3: CLOUD STORAGE / DATA LAKE ARCHITECTURE (Bottom-Left Storage Mapping)
# ------------------------------------------------------------------------------
# Hierarchical levels broken down visually:
#   - Level 1 (Slowest): Connects to top-level Cloud Data Storage Containers ('C')
#   - Level 2 (Medium):  Drills down into named sub-directories or Folders ('f') 
#   - Level 3 (Fastest): Reaches the terminal level to process raw file documents

for c in Containers:                   # Level 1: Scans top cloud buckets/containers
    for f in folders:                  # Level 2: Enters directories inside the active container
        for file in files: 
            pass            # Level 3: targets files inside the current folder path
            # Do Something             # Target: Reads, converts, or processes individual objects