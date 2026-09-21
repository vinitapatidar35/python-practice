n = int(input()) # for single int it handle well and if you give multiple value like 1 2 3 4 or anything int dont know space
arr = list(map(int , input.split())) # we need to create map for so first split the input and then cahne to int each 

ans = set(arr) # for removing duplicate
#Sort them (sorted() automatically turns the set back into a sorted list!)
# and sorted list is different list not use the actual list create new sorted list 
my_final_ans = sorted(ans)
print(my_final_ans[-2])


n = int(input())
arr = list(map(int, input().split()))

# 1. Validate n
# 2. Validate arr: Check if All elements are within -100 and 101
if (n in range(2, 11)) and all(score in range(-100, 101) for score in arr):
    
    # If valid, run your clean logic:
    unique = set(arr)
    my_final_ans = sorted(unique)
    print(my_final_ans[-2])
    
else:
    print("Invalid input: Constraints violated.") 