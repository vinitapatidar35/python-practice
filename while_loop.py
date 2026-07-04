
"""
while_loop.py

Covers:
- while loop basics (indefinite iteration based on a condition)
- for loop vs while loop: iteration type, state management, infinite loop risk,
  best use cases
- Manual counter tracking (initialize, check, update)
- while True with break as an exit condition
- Attempt-limiting pattern (loop with a max retry counter)
"""

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