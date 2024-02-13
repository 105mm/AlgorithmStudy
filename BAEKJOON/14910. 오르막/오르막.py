import sys

N = list(map(int, sys.stdin.readline().strip().split()))

M = sorted(N)

if N == M:
    print("Good")

else:
    print("Bad")