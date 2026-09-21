n = int(input()) # number of students

students = []
actual_marks_list = []

for stu in range(1,(n+1)):
    name = input()
    marks = float(input())
    students.append([name,marks])

mark = []    
for stu in students:
    mark.append(stu[1])
    
my_original = set(mark)
ans = sorted(my_original)
actual_result = ans[1]

for stu in students:
    if stu[1] == actual_result:
        final = actual_marks_list.append(stu[0])
 
for name in sorted(actual_marks_list):       
    print(name)
    
    
