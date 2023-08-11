a= list(input())

sum = 10

for i in range (len(a)-1):
    if a[i]==a[i+1]:
        sum += 5
    elif a[i]!=a[i+1]:
        sum += 10

print(sum)


"""
for i in range (len(a)-1):
리스트의 마지막 원소를 생략한다.
"""