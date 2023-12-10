import sys

black = 0

N, M = map(int, sys.stdin.readline().strip().split())

card = list(map(int, sys.stdin.readline().strip().split()))


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if black < sum <= M:
                black = sum


print(black)