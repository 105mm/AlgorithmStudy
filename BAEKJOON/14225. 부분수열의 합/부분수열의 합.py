import sys

a = int(sys.stdin.readline().strip())

b = list(map(int, sys.stdin.readline().strip().split()[:a]))

count = 1

while count < a:
    
    for i in range(a-1):
        for j in range(i+count, a):
            if sum(b[i:j]) not in b:
                b.append(sum(b[i:j]))
    
    count += 1

print(b)

"""
3 5 1 2

01 02 03 12 13 23

012 013 023 123

0123


3 5 1 2 4

01 02 03 04 12 13 14 23 24 34

012 013 014 023 024 034 123 124 134 234

0123 0124 0234 1234

012345


"""


