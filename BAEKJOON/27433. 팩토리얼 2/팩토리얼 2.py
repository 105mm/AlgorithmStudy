import sys

N1 = int(sys.stdin.readline().strip())

P1 = 1
for i in range (N1, 0, -1):
    P1 *= i

print (P1)