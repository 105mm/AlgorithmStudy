import sys

list_yut = ["E", "A", "B", "C", "D"]

for _ in range(3):
    count_yut = 0
    list_0 = list(map(int, sys.stdin.readline().strip().split()[:4]))
    for i in list_0:
        if i == 0:
            count_yut += 1
    print(list_yut[count_yut])

""" 
SUM 활용

for _ in range(3):
    l = list(map(int, input().split()))
    n = sum(l)
    if n==1:
        print('C')
    elif n==2:
        print('B')
    elif n==3:
        print('A')
    elif n==4:
        print('E')
    else:
        print('D')

"""