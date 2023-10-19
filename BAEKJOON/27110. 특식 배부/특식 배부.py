import sys

N1 = int(sys.stdin.readline().strip())

list_1 = list(map(int, sys.stdin.readline().strip().split()[:3]))

result = 0

for i in list_1:
    if i <= N1:
        result += i
    
    if i > N1:
        result += N1

print (result)