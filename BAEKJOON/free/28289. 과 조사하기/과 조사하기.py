p = int(input())

count_free = 0
count_soft = 0
count_im = 0
count_ai = 0

for _ in range (p):
    grade, clas, num = map(int, input().split())

    if grade == 1:
        count_free += 1
        
    if grade != 1 and (clas == 1 or clas == 2):
        count_soft += 1
        
    if grade != 1 and clas == 3:
        count_im += 1
        
    if grade != 1 and clas == 4:
        count_ai += 1


print(count_soft)
print(count_im)
print(count_ai)
print(count_free)