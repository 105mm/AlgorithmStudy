import sys

n = int(sys.stdin.readline().strip())

result = 0

for i in range(1, n + 1):
    term = sum(range(1, i + 1)) + i*(i+1)
    result += term

print (result)