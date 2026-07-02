# first explain all the data structures and difference beyween them

# list : orderd , duplicate allow , we can access element by position number , indexed , mutable(change after creating a list)

# tuple
# orderd collection , immutable , allow duplicates , indexed
my_tuple = (10,20,30,40,10)
print(sorted(my_tuple)) # output of this function always gonna be list

# set : unordered collection of unique values , 
my_set = {10,20,30}
print(my_set) # no order on ans 
my_set = {10,20,30,10} 
print(my_set)# no duplicate in result
#print(my_set[0]) not indexed
print(my_set.remove(20))# mutable

# set methods
a = {10,20,30,34}
a.add(90)
a.add(34)
print(a)
a.update("hy")
a.update([1,2,3]) # added in set not as a whole list but only value inside of iterable
print(a)
# we can also use math operator as quick sortcut
a |= {"hello"} #same as a.update()
print(a)
a.remove(34) # throw an error if its not exist in set
print(a)
a.discard(99) # not give error if its available discard it otherwise nothing
print(a)
a.pop() # remove any random value from set

b = {1,2,3,4,5.10,30,40}
c = {100,90,30,1,2,7,87}
# mathematical operation
print(a.union(b))
print(a | b) # same as union
print(a.intersection(b))
print(a & b) # same as intersection
print(a.difference(b))
print(a - b)# same as difference
print(a.symmetric_difference(b)) # not overlapping at all from both sets
print(a ^ b) # same as symmetric_difference

print(a.issubset(b))# means everything present in a present in b, all item of a present in b
print(a.issuperset(b))
print(a.isdisjoint(b)) # shares no same items

