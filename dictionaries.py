"""
dictionaries.py

Covers:
- Dictionary basics: key-value pairs, unique keys, mutability
- Accessing values via key vs .get() (with default fallback)
- Membership checks with in / not in
- View objects: keys(), values(), items()
- Iterating over a dict (keys only, and with .items())
- Adding, updating, removing entries
- pop() with default value, popitem()
- dict.fromkeys() to build a dict with a shared default value
- Building a new dict with a for loop + condition
- Dict comprehension with condition
"""

my_dict = {"a" : 1,
           "b" : 2,
           "c" : 5
           }
print(my_dict)
print(my_dict['a'])
my_dict["c"] = 80
print(my_dict)

user = {"id" : 1, "age" : 25 , "city" : "berlin"}
user["name"] = 'Vinita'
print(user.get("name"))
print(user.get("name", "unknown"))

print("age" in my_dict)
print("name" in my_dict)
print("name" not in my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

for u in user:
    print(u)
    print(user[u])

for x, y in user.items():
    print(x , y)

user["dream"] = "stable and independent life"
print(user)
user["age"] = 21
user.update({"country" : "Japan", "taste" : "sweet"})
print(user)
taste = user.pop("taste")
print(taste)
print(user)

user.pop("salary", "not mentioned")
user.popitem()

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