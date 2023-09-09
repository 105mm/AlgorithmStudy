import sys

a = int(sys.stdin.readline().strip())
total = 0

for _ in range(a):
    b = int(sys.stdin.readline().strip())
    total += b

print(total - (a - 1))