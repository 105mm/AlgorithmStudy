import sys

a,b = map(int, sys.stdin.readline().strip().split())

list_yak = []

for i in range (1, a//2+1):
    if a%i == 0:
        list_yak.append(i)
list_yak.append(a)


if len(list_yak)>=b:
    print (list_yak[b-1])

else:
    print (0)