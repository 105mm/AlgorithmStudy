import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N1, N2, N3, N4, N5 = map(float, sys.stdin.readline().strip().split())

    result = N2 / ((N3 + N4) / N5)

    print(int(N1), f"{result:.6f}")