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



"""
간단버전
c = [0,0,0,0]
for i in range(int(input())):
    a,b,_ = map(int,input().split())
    if a==1:c[3]+=1
    elif b==4:c[2]+=1
    elif b==3:c[1]+=1
    else:c[0]+=1
for i in range(4):print(c[i])

"""