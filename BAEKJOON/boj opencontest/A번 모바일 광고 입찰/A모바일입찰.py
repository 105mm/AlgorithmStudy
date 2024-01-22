import sys

N, K = map(int, sys.stdin.readline().strip().split())

mi = []

count = 0

for _ in range(N):
    A, B = map(int, sys.stdin.readline().strip().split())

    if (A - B) < 0:
        mi.append(A - B)

    if (A - B) >= 0:
        count += 1

mi.sort(reverse=True)

if count >= K:
    print(0)
else:
    print(abs(mi[K - count - 1]))