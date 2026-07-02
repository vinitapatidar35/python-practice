# dictionaries data structure in python
my_dict = {"a" : 1,
           "b" : 2,
           "c" : 5
           }
print(my_dict) # ordered , no duplicate key must be unique
print(my_dict['a']) # not indexed we can get output with the help of key value
my_dict["c"] = 80 # mutable
print(my_dict)

user = {"id" : 1, "age" : 25 , "city" : "berlin"}
user["name"] = 'Vinita'
#print(user["role"]) when u are not sure about key python give us error so we use get
print(user.get("name")) # if key available give us a value othrwise None
print(user.get("name", "unknown")) # we can give alternatievly for None its unknown

# checks 
print("age" in my_dict)
print("name" in my_dict)
print("name" not in my_dict)

# view objects
print(my_dict.keys()) # all the keys, list of keys
print(my_dict.values()) # all teh values, list of values
print(my_dict.items()) # all key value pair, lit of tuples

for u in user:
    print(u)# we get keys only
    print(user[u]) # we get values

for x, y in user.items():
    print(x , y)

# add, remove,update
user["dream"] = "stable and independent life" # add
print(user)
user["age"] = 21 # update
user.update({"country" : "Japan", "taste" : "sweet"})
print(user)
taste = user.pop("taste")
print(taste)
print(user)

user.pop("salary", "not mentioned")# user.pop("salary") not a key breaking whole program give a error we need to define default value if key is notdefine
user.popitem()# return and delete thhe most recent key value pair from the dictionary 
 
 # fromkeys()
 #build a  dic where all keys get the same default value
new_dic = dict.fromkeys(["student name", "age" , "class" , "roll no."],"initiate empty")
print(new_dic)
new_dic = dict.fromkeys(["student name", "age" , "class" , "roll no."],0)
print(new_dic)
user["age"] = 9

user = {"id" : 1, "name": "vinita", "age" : 20, "city" :"Berlin"}
new = {}
for x, y in user.items():
    if  isinstance(y,str) and y.isalpha() :
        new[x] = y
print(new)

user_string = {
    k : v.upper()
    for k,v in user.items()
    if isinstance(v,str)
}
print(user_string)