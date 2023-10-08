import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    N, K = map(int, sys.stdin.readline().strip().split())
    if N < K:
        print("NO BRAINS")
    elif N > K:
        print("MMM BRAINS")
    else:
        print("MMM BRAINS")