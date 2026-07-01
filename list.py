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

# nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
# how to read matrix
print(matrix[1][1])#5
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
#matrix.sort()

# indexing and slicing
lst = ["a", "b", "c","d","e"]
print(lst[1])
print(lst[::-1])
print(lst[2:4])
print(lst[-1])


# unpacking list
my_fav_person_detail = ["vinita", "21" , "japan" , "data engineer" , "world tour" , "lots of money"]
name , age , dream_country , role , big_wishlist , hapiness = my_fav_person_detail
print(dream_country)
print(hapiness)

# rest collection asterisk *details
my_fav_person_detail = ["vinita", "21" , "japan" , "data engineer" , "world tour" , "lots of money"]
name, *details , hapiness = my_fav_person_detail
print(name)
print(details)
print(hapiness)
#*details,age , dream_country ,*details
name , *other = my_fav_person_detail
print(name)
# only one (*) is allowed in unpacking, after * any word you can use
# unpacking rule
#1.no of variable must be matching
#2.you can unpack any sequence (list , tuple , string etc)
str = "hello"
one,two,*other = str
print(one)
print(two)
print(other)
#3. skipping cahracter_underscore (_)
lst = ["vinita", "21" ,"India", "study"]
name , _ , country , _ = lst
print(name)
print(_)
print(country)
print(_)
#4. we can combine * and _
lst = ["vinita", "21" ,"India", "study"]
first , *_ , last = lst
print(first)
print(*_)

# explore and analyze the data
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

# change the data
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
copy_letters = original_letters # both list reference the same list in memory
print(copy_letters)
print(original_letters)
copy_letters.append("g")
print(copy_letters)
print(original_letters)

#shallow copy
letters = ['a','b','d','c']
copy_letters = letters.copy() # creates a seperate list in memory
letters.append("you girl")
print(letters)
print(copy_letters)

# deep copy
# need to use deepcopy() from copy module need to import copy ,
# sahllow copy copy from one level not deeply 

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
matrix_copy = copy.deepcopy(matrix_1) # creates a true , independent new copy for all levels 
matrix_1.pop()
matrix_1.append("shitt")
print(matrix_1)
print(matrix_copy)

# copy.copy() same as our shallow copy new_list_name = old_list_name.copy()

lst = [1,2,3]
copy1 = lst
print(copy1 is lst)
new_copy = lst.copy()
print(new_copy is lst)

# shallow copy sahring a same child 
# for 1 dimension copy is enough no child so shallow copy is enough
# for more than 1-d we need deep copy
# always try to make extra copy for experiment and test

# combine list
letters = ['a' , 'b' ]
num = [1,2,3]
comb = letters + num
print(comb)
print(letters * 2)
comb = [letters , num] 
print(comb)
    
print(letters.extend(num)) #expand the original one
print(letters)
print(num)

# pair the item from 2 diff list 1st item of 1st list with 1st item of second list
#output of zip is list of tupple
# pair up len(min(list1,list2))
# output iterator and object we need to convert in thelist
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

#iterators and iterables
alph = ['a','b','c','d']
for x in alph:
    print(x)

alph = ['a','b','c','d']
new = []
for x in alph:
    new.append(x.upper())
print(new)
               
# enumerate
# default is 0 but we can choose start number for index , object , need to type list
alph = ['a','b','c','d']
print(list(enumerate(alph)))
print(list(enumerate(alph, start = 1)))
for index,value in enumerate(alph):
    print(index , value)

#reversed()
alph = ['a','b','c','d']
print(reversed(alph))
print(list(reversed(alph)))
alph = ['a','b','c','d']
for i in reversed(alph):
    print(i)

# what is iterator obj like why we need to write list in front of that otherwise showing list_someiterator


