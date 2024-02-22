import sys

N1 = int(sys.stdin.readline().strip())
N2 = int(sys.stdin.readline().strip())
N3 = int(sys.stdin.readline().strip())

N_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

N = N1 * N2 * N3

N_str = str(N)

for i in N_str:
    N_list[int(i)] += 1

for i in range(10):
    print(N_list[i])


"""
while N > 0:
    digit = N % 10
    N //= 10
    N_list[digit] += 1
"""