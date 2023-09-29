import sys

a = int(sys.stdin.readline().strip())

list_yut = []

combo = 0

result = 0

list_0 = list(map(int, sys.stdin.readline().strip().split()[:a]))

for i in list_0:
    if i == 1:
        combo += 1
        result += combo
    elif i == 0:
        combo = 0

print(result)