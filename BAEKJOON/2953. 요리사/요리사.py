import sys

result=0

for i in range(5):
    N = sum(list(map(int, sys.stdin.readline().strip().split())))

    if N > result:
        rank = i+1
        result = N

print(rank, result)