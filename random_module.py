"""
random_module.py

Covers:
- random module basics (pseudo-random numbers, seed concept)
- random.randint(start, stop) - inclusive integer range
- random.random() - float between 0.0 and 1.0
- random.uniform(start, stop) - float within custom range
- random.choice(seq) - pick one item (non-destructive)
- random.shuffle(list) - reorders list in-place (destructive)
- random.seed(value) - makes random sequence repeatable
"""

import random

print(random.randint(1, 6))

print(random.random())

print(random.uniform(10.5, 20.5))


items = ["Gold", "Silver", "Bronze"]

print(random.choice(items))

random.shuffle(items)
print(items)


random.seed(10)
print(random.randint(1, 100))
print(random.randint(1, 100))


print(random.random())
print(random.randint(1,int(random.random()*1000)))
print(random.randint(23,78))