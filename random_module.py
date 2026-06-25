# 💡 THEORY: 'random' is a built-in module. It uses mathematical formulas 
#    to generate "Pseudo-Random" numbers starting from a base value called a "seed".

import random

# --- 1. GENERATING NUMBERS ----------------------------------------------------
# random.randint(start, stop) -> Generates an int. BOTH boundaries are INCLUDED!
print(random.randint(1, 6))      # Output: 1, 2, 3, 4, 5, or 6

# random.random() -> Generates a float between 0.0 (inclusive) and 1.0 (exclusive)
print(random.random())           # Output: e.g., 0.472918...

# random.uniform(start, stop) -> Generates a precise float within a custom range
print(random.uniform(10.5, 20.5)) # Output: e.g., 14.8234...


# --- 2. WORKING WITH SEQUENCES (LISTS / STRINGS) ------------------------------
items = ["Gold", "Silver", "Bronze"]

# random.choice(seq) -> READ-ONLY. Randomly selects exactly one item from a list/string.
print(random.choice(items))      # Output: e.g., "Silver" (Original list is untouched)

# random.shuffle(list) -> DESTRUCTIVE/IN-PLACE mutation. Reorders the actual list.
random.shuffle(items)            
print(items)                     # Output: The 'items' variable is now permanently rearranged!


# --- 3. REPEATABLE RANDOMNESS (THE SEED) --------------------------------------
# random.seed(value) -> Locks the random number generator to a fixed math pattern.
# It does NOT force the output to equal the seed value; it forces the random 
# sequence to be completely identical every single time you run your script.

random.seed(10)
print(random.randint(1, 100))    # Will ALWAYS print 74 on the 1st run
print(random.randint(1, 100))    # Will ALWAYS print 5  on the 2nd run


print(random.random())
print(random.randint(1,int(random.random()*1000)))
print(random.randint(23,78))