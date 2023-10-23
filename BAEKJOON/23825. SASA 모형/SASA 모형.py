import sys

N, K = map(int, sys.stdin.readline().strip().split())

if N//2 == K//2:
    print(N//2)

else:
    print(min(N//2, K//2))