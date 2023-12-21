import sys

N1 = int(sys.stdin.readline().strip())

if N1 % 2 == 0:
    print ((N1//2 + 1 ) ** 2)

else:
    print ((N1//2 + 1) * (N1//2 + 2))