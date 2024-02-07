import sys

N = int(sys.stdin.readline().strip())

for _ in range (N):
    
    N1, N2 = map(int, sys.stdin.readline().strip().split())

    print(N2*2-N1, N2-(N2*2-N1))