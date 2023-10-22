import sys

N, K = map(int, sys.stdin.readline().strip().split())

if N - N*K/100 < 100 :
    print(1)

else:
    print(0)