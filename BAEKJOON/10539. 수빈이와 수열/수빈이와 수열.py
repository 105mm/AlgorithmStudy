import sys

N1 = int(sys.stdin.readline().strip())

M1 = list(map(int, sys.stdin.readline().strip().split()))

result = []

result.append(M1[0])

for i in range (1, N1):

    result.append((i + 1) * M1[i] - sum(result[:i]))

for i in result:
    print(i, end=' ')