import sys

a = int(sys.stdin.readline().strip())

result = 1

for i in range (a, 0, -1):
    result *= i

print (result)