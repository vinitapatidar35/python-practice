"""
list.py

Covers:
- Creating lists (empty, literal, list(), list(range()), list(string))
- Nested lists / matrices - indexing, slicing, modifying nested elements
- List indexing and slicing
- Unpacking lists: basic unpacking, rest collection with *, skipping with _,
  combining * and _
- Analyzing data: max, min, len, sum, all, any
- count(), index()
- Membership operators: in, not in
- List comparison: ==, is, < (lexicographic)
- Mutating methods: append, insert, clear, remove, pop, sort, reverse
- sorted() vs .sort(), reversed() vs .reverse()
- Reference assignment vs shallow copy (.copy()) vs deep copy (copy.deepcopy())
- Combining lists: +, *, extend()
- zip() to pair elements from multiple iterables
- Iterating with for loops, enumerate()
- map() to transform iterables
- filter() to filter iterables (including filter(None, ...))
- isinstance() for type checking
"""

import copy

empty = []
print(empty)
print(type(empty))

letters = ["a", "b" , "c"]
print(letters)

mixed_list = [[1,2,3] , 5.66 , "hyee" , {"dic" : "yes", "num" : 78}]
print(mixed_list)

empty_list = list()
print(empty_list)
name = list("boraaa")
print(name)

num_list = list(range(1,51))
print(num_list)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][1])
print(matrix[0][2])
print(matrix[0])
print(matrix[-1])
print(matrix[-1][-2])
print(matrix[-1][1])
print(matrix[0][::])
print(matrix[0][1:])
print(matrix[2][::])
print(matrix[1].append("x"))
print(matrix[1].remove("x"))
matrix[0] = ['a','b','d']
matrix[0][0] = "hyee"

lst = ["a", "b", "c","d","e"]
print(lst[1])
print(lst[::-1])
print(lst[2:4])
print(lst[-1])

my_fav_person_detail = ["vinita", "21" , "japan" , "data engineer" , "world tour" , "lots of money"]
name , age , dream_country , role , big_wishlist , hapiness = my_fav_person_detail
print(dream_country)
print(hapiness)

my_fav_person_detail = ["vinita", "21" , "japan" , "data engineer" , "world tour" , "lots of money"]
name, *details , hapiness = my_fav_person_detail
print(name)
print(details)
print(hapiness)

name , *other = my_fav_person_detail
print(name)

stri = "hello"
one,two,*other = stri
print(one)
print(two)
print(other)

lst = ["vinita", "21" ,"India", "study"]
name , _ , country , _ = lst
print(name)
print(_)
print(country)
print(_)

lst = ["vinita", "21" ,"India", "study"]
first , *_ , last = lst
print(first)
print(*_)

num = [1,2,3,4,5,6]
print(max(num))
print(min(num))
print(len(num))
print(sum(num))
print(all(num))
print(any(num))

num1 = ["", [] ,()]
print(all(num1))
print(any(num1))
num2 = ["", [] ,(),(1)]
print(any(num2))

num = [1,2,3,4,5,6,1,3,4,5,6,6,7,6,5,4,3]
print(num.count(7))
print(num.count(5))
print(num.index(3))
print(num.index(1))

print(1 in num)
print("a" in num)
print(10 not in num)

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)
print(list1 is list2)

list1 = [1,5,3]
list2 = [1,2,3]
print(list2 < list1)

data = [100,1000,88,768,999]
data.append(10009)
data.insert(1,45)

list1 = [1,2,3,4,-1,9]
print(list1.clear())

list1 = [1,2,3,4,-1,9]
print(list1.remove(-1))
print(list1.pop()) 
print(list1.pop(0)) 

letter = ['a', 'b' , 'b', 'c' , 'v']
letter[1] = 'h'
print(letter)
print(letter.sort())
print(letter.sort(reverse=True))

sort_list = [1,5,3,10,100,99,98,56]
print(sort_list.sort())
print(sort_list.sort(reverse=True))

sort_list = [1,5,3,10,100,99,98,56]
new_list = sorted(sort_list)
print(new_list)
print(sort_list)
new_list = sorted(sort_list, reverse=True)

sort_list = [1,5,3,10,100,99,98,56]
print(sort_list.reverse())
sort_list = [1,5,3,10,100,99,98,56]
neww_list = reversed(sort_list)
print(neww_list)
neww_list = list(reversed(sort_list))
print(neww_list)

original_letters = ['a','b','d','c']
copy_letters = original_letters
print(copy_letters)
print(original_letters)
copy_letters.append("g")
print(copy_letters)
print(original_letters)

letters = ['a','b','d','c']
copy_letters = letters.copy()
letters.append("you girl")
print(letters)
print(copy_letters)

shallow_copy  = ['a' , 'b' , 'c' , "d"]
new_one = shallow_copy.copy()
new_one.pop()
print(new_one)
print(shallow_copy)
shallow_copy.append("hyee beautiful")
print(new_one)
print(shallow_copy)

matrix_1 = [['a','b'],['c','d']]
matrix_copy = matrix_1.copy()
matrix_1.pop()
matrix_1.append("shitt")
print(matrix_1)
print(matrix_copy)

matrix_1 = [['a','b'],['c','d']]
matrix_copy = copy.deepcopy(matrix_1)
matrix_1.pop()
matrix_1.append("shitt")
print(matrix_1)
print(matrix_copy)

lst = [1,2,3]
copy1 = lst
print(copy1 is lst)
new_copy = lst.copy()
print(new_copy is lst)

letters = ['a' , 'b' ]
num = [1,2,3]
comb = letters + num
print(comb)
print(letters * 2)
comb = [letters , num] 
print(comb)

print(letters.extend(num))
print(letters)
print(num)

letters = ['a' , 'b','c' , 'd']
num = [1,2,3]
comb = list(zip(letters , num))
print(comb)
comb = list(zip(letters , num , "hyee"))
print(comb)
comb = list(zip(letters , num , "hy"))
print(comb)

ids = [101, 102 , 103]
name = ['ali', 'sara','zara']
data = list(zip(ids,name))
print(data)

alph = ['a','b','c','d']
for x in alph:
    print(x)

alph = ['a','b','c','d']
new = []
for x in alph:
    new.append(x.upper())
print(new)

alph = ['a','b','c','d']
print(list(enumerate(alph)))
print(list(enumerate(alph, start = 1)))
for index,value in enumerate(alph):
    print(index , value)

alph = ['a','b','c','d']
print(reversed(alph))
print(list(reversed(alph)))
alph = ['a','b','c','d']
for i in reversed(alph):
    print(i)

alph = ['a','b','c','d']
print(list(map(str.upper,alph)))

num =["1","2","3","4","5"]
print(list(map(int ,num )))

num_alph = ["vinita" , "hyee" , 980 , 678 , "876"]
print(list(filter(lambda x : isinstance(x,str) and x.isalpha(), num_alph)))

num = ["hyy" , "" , False , None ,"good morning"]
print(list(filter(None, num)))

num_alph = ["vinita" , "hyee" , "980" , "678" , "876"]
print(list(filter(str.isalpha , num_alph)))

for i in filter(str.isalpha , num_alph):
    print(i)

x = "vinita"
y = 980

print(isinstance(x, str))
print(isinstance(y, str))