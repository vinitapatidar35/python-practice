
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

#The Golden Rule of while True
#Never use a while True loop without a break statement attached to an if condition. 
#If you forget it, your code will get stuck in a locked loop, freezing 
#your terminal until you forcefully kill it (usually by hitting Ctrl + C).
user="" 
count = 0
while True:
    user = input("type 1 only")
    if count == 3:
        break 
print('you type 1 in 3 times good girl/boy')
