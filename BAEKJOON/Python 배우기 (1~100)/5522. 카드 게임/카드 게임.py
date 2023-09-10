import sys

b=0

for _ in range(5):
    a = int(sys.stdin.readline().strip())

    b += a

print(b)