import sys

a = int(input())

for _ in range(a):
    N, K = map(int, sys.stdin.readline().strip().split())

    count = 0

    for i in range (1, N):
        for j in range (i+1, N):
            if ((i**2 + j**2 + K) % (i*j)) == 0:
                count += 1
    
    print (count)