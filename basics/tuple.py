"""
tuple.py

Covers:
- Data structures overview: list vs tuple vs set (ordering, mutability, duplicates, indexing)
- Tuple basics: ordered, immutable, allows duplicates, indexed
- sorted() on a tuple returns a list
- Set basics: unordered, unique values only, mutable, not indexed
- Set methods: add, update, remove, discard, pop
- Set operators as shortcuts: |= for update
- Set mathematical operations: union, intersection, difference, symmetric_difference
  (and their operator equivalents |, &, -, ^)
- Set relational checks: issubset, issuperset, isdisjoint
"""

my_tuple = (10,20,30,40,10)
print(sorted(my_tuple))

my_set = {10,20,30}
print(my_set)
my_set = {10,20,30,10}
print(my_set)
print(my_set.remove(20))

a = {10,20,30,34}
a.add(90)
a.add(34)
print(a)
a.update("hy")
a.update([1,2,3])
print(a)
a |= {"hello"}
print(a)
a.remove(34)
print(a)
a.discard(99)
print(a)
a.pop()

b = {1,2,3,4,5.10,30,40}
c = {100,90,30,1,2,7,87}

print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)

print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))