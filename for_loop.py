"""
for_loop.py

Covers:
- for loop over a list and over a string
- range(stop), range(start, stop), range(start, stop, step)
- while loop with a state modifier
- break, continue, pass
- for...else (else runs only if loop completes without break)
- print() end and sep parameters
- Practical patterns: sum accumulation, string cleanup pipeline, multiplication
  table, star patterns, duplicate detection, batch email validation
- Nested for loops (2-level: combinations; 3-level: hierarchical data
  traversal examples for time-series, database tables, and cloud storage)
"""

grocery_list = ["eggs", "milk", "bread"]

for item in grocery_list:
    print(f"Pipeline processing inventory item: {item}")


word = "CODE"

for letter in word:
    print(f"Extracting character slice: {letter}")


for i in range(3):
    print(f"Default zero-indexed step count: {i}")

for i in range(5, 8):
    print(f"Bounded range step count: {i}")

for i in range(10, 21, 5):
    print(f"Stepped range count: {i}")


battery_power = 3

while battery_power > 0:
    print(f"Device running. Remaining charge: {battery_power}%")
    battery_power -= 1

print("System Alert: Battery dead. Shutdown complete.")


for score in range(1, 10):
    if score == 4:
        print("Target threshold hit! Emergency break triggered.")
        break
    print(f"Score registered: {score}")


for floor in range(1, 6):
    if floor == 3:
        print("Floor 3 under construction. Skipping!")
        continue
    print(f"Elevator opening at floor: {floor}")


search_target = "admin_access"
permissions = ["guest_view", "user_edit", "moderator_delete"]

for permission in permissions:
    if permission == search_target:
        print("Access Granted!")
        break
else:
    print(f"Security Alert: '{search_target}' not found anywhere in list.")


incoming_batch = ["user1@gmail.com", "bad_email_no_at.com", "admin@org.net"]

for email_to_test in incoming_batch:
    if not ('@' in email_to_test and '.' in email_to_test):
        print(f"REJECTED: '{email_to_test}' failed basic symbol integrity.")
        continue
    print(f"APPROVED: '{email_to_test}' successfully queued for dispatch.")

i = 1
for i in range(6):
    print(f"ROUND : {i}")
    i = i + 1

items = (1,2,3,4,5,6,7)
for item in items:
    print(f"i have {item} chocolate")

name = "Vinita"
for letter in name:
    print(letter, end = " ")

scores = [80,90,99,87,76]
sum = 0
for score in scores:
    sum = sum + score
print("\n", sum)

files = ["datA.csv " , " file.txt  " , "endinG.TXT"]
for file in files:
    x = file.strip().lower().replace("csv", "txt")
    print(x)

for x in range(11):
    print(f"7 * {x} = {7 * x}")

for x in range(6):
    print("*" * x)

row = 6
for x in range(1 , row +1):
    spaces = " "  * (row - x)
    star = "*" * x
    print(f"{spaces}{star}")

names = ['maria', "arena" ," " ,"luca" , "messi" ]
for name in names:
    if name == " ":
        pass
    else:
        print(name)

for name in names:
    if name == "luca":
        continue
    else:
        print(name)    

for name in names:
    if name == "arena":
        break
    else:
        print(name)

week_days = ["Mon", "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]

for week_day in week_days:
    if week_day == "Mon" or week_day == "Tue" or week_day == "Wed" or week_day == "Thu" or week_day == "Fri":
        print("hurreee working days: " + week_day)
    else:
        pass

list = [1,2,3]
for item in list:
    print(f"{item}")
else:
    print("no item ")


names = ["maria", "arena", "luca", "messi"]

for name in names:
    if name == "luca":
        print("Found luca! Breaking out of loop.")
        break
else:
    print("Alert: The target name was not found in the list.")

for name in names:
    if name == "vinita":
        print("Found vinita! Breaking out of loop.")
        break
else:
    print("Alert: 'vinita' was not found in the list.")


names = ["alifia", "saddow" , "bunna" ,None,"brozza"]
for name in names:
    if name == None:
        print("Error in Data , missing value ")
        break
else:
    print("no missing anme , everything is right in data.")

Files = ["data.csv", "study.csv" , "school.csv", "student.txt"]
for file in Files:
    if file.endswith(".txt"):
        x = file.replace(".txt",".csv")
        print(x)
    else:
        print(file)
else:
    print("all files are csv files.")

Files = ["data.csv", "study.csv" , "school.csv", "student.txt"]
for file in Files:
    if file.endswith(".txt"):
        print("unnecessary file")
        break 
else:
    print("clean required file")

files = ["data.csv", "study.csv" , "school.csv", "student.txt",  "school.csv", "student.txt"]
seen_files = []
for file in files:
    if file in seen_files:
        print("found duplicate")
        break
    else:
        seen_files.append(file)
else:
    print("all are unique file")


for x in range(3):
    for y in range(2):
        print(f"{x * y}")
        print(f"{x},{y}")
        print("\n") 

colors = ["red" , "blue" , "green" , "golden" , "silver"]
tshirts = ["one", "two"]
count = 0

for color in colors:
    for tshirt in tshirts:
        print(f"count total number of combination {color}, {tshirt} {count} combination")
        count = count + 1
print(f"total number of combination {count}")


# NOTE: the three loops below are conceptual/illustrative structure examples -
# years, months, days, tables, columns, rows, Containers, folders are not
# actually defined, so these blocks are for structure reference only.

for year in years:
    for month in months:
        for day in days:  
            pass

for table in tables:
    for col in columns:
        for row in rows:  
            pass

for c in Containers:
    for f in folders:
        for file in files: 
            pass