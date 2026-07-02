#lambda function
lst = [1,2,3,4,5]
new = []
ans = lambda x : x * 2
for x in lst:
    result = ans(x)
    print(result)
    new.append(result)
print(new)

multiply = lambda x : x * 2
print(multiply(6))

arith = lambda x , y , z : x + y - z
print(arith(5,6,4))

# lambda can contain any expresion , including conditions
check = lambda i : i in "python"
print(check("n"))

# lambda + map
dic = [("python", "hyeee")]
result = (list(map(lambda item: item[0].isalpha() and item[1].isalpha() and isinstance(item[0],str) and  isinstance(item[1],str) , dic)))
print(result)

prices = ["$103.00" , "$567.99" , "$23.50"]
flt = lambda p : float(p.replace("$",""))
for price in prices:
    print(flt(price))

print(list(map(lambda p : float(p.replace("$","")), prices)))

rent = [1000, 980 , 120 , 89, 678 , 87]
cal = lambda x : x > 100
print(list(filter(lambda x : x > 100, rent)))

lst1 = [["maria", 90],
        ["hexan", 44],
        ["era", 78]]
print(list(filter(lambda x : x[1] > 50, lst1)))
print(list(filter(lambda x : x[0].startswith("m"), lst1)))

# list comprehension
price = [45,65,34,22,90]
result = [p for p in price if p > 33]
print(result)

data = ["Www.Vinita@gmail.com","www.mUskan@gmail.com  ","  www.preety@gmail.com"]
result = [x.strip().lower().replace("www.", "") for x in data ]
print(result)