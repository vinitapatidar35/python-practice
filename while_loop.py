
# 💡 WHILE LOOP DEFINITION:
# A control flow statement that repeatedly executes a block of code as long as 
# a specified boolean condition remains True. It is an "indefinite loop" 
# because it keeps running until its condition changes to False or it hits a break.

# ==============================================================================
# KEY DIFFERENCES: FOR LOOP vs. WHILE LOOP
# ==============================================================================

# 💡 1. ITERATION TYPE (DEFINITE vs. INDEFINITE):
#   - FOR LOOP: Used for definite iteration. It runs a predetermined, fixed 
#     number of times based on the size of the sequence it is stepping through.
#   - WHILE LOOP: Used for indefinite iteration. The exact number of cycles 
#     is unknown beforehand; it repeats entirely based on a dynamic condition.

# 💡 2. STATE AND VARIABLE MANAGEMENT:
#   - FOR LOOP: Automates state control. It initializes, updates, and 
#     terminates the loop variable automatically as it traverses an iterable.
#   - WHILE LOOP: Requires manual control. You must explicitly initialize a 
#     tracking variable before the loop and manually update it inside the block.

# 💡 3. RISK OF INFINITE LOOPS:
#   - FOR LOOP: Highly secure. It naturally terminates the moment it reaches 
#     the end of its sequence, collection, or range pipeline.
#   - WHILE LOOP: High risk of infinite loops. If the conditional statement 
#     never evaluates to False (due to a missing manual update), it runs forever.

# 💡 4. OPTIMAL REAL-WORLD USE CASES:
#   - FOR LOOP: Perfect for traversing data structures (lists, tuples, dicts) 
#     and running code blocks across explicit, structured numeric ranges.
#   - WHILE LOOP: Perfect for tracking state-driven tasks like reading input streams, 
#     maintaining game states, or waiting for specific event triggers.
i = 0
while i < 4:
    print(f"{i}")
    i = i + 1

user = ""
while user != "yes":
    user = input("type only yes: ")
print("you are right")

while True:
    user = input("type yes only ")
    if user == "yes":
        break
print('thank you for typing yes only')


attempts = 0  
while True:
    answer = input("Do you agree? (yes/no): ")
    attempts += 1  
    
    if answer == "yes":
        print("Glad we are on the same page")
        break
        
    if attempts == 3:
        print("Maximum attempts reached.")
        break

print("Thank You")