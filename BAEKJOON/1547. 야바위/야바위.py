import sys

ball = 1

a = int(input())

for _ in range(a):
    N, K = map(int, sys.stdin.readline().strip().split())

    if N == ball:
        ball = K
    elif K == ball:
        ball = N
    
    else:
        pass

print(ball)