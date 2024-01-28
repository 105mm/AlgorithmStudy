import sys

N1, N2 = map(int, sys.stdin.readline().strip().split())

sum = 0

cnt = 0

num = list(map(int, sys.stdin.readline().strip().split()[:N1]))

for i in range(N1):
    sum += num[i]

    if sum > N2:
        break

    cnt += 1

print(cnt)