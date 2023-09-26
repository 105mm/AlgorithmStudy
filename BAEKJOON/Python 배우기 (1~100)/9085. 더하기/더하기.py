import sys

a = int(sys.stdin.readline().strip())


for _ in range (a):
    list_0 = []
    b= int(sys.stdin.readline().strip())
    list_0 = list(map(int, sys.stdin.readline().strip().split()[:b]))
    print(sum(list_0))