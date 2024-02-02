import sys

N, K = map(int, sys.stdin.readline().strip().split())

num_list = list(range(1, N+1))

for _ in range (K):
    N1, N2 = map(int, sys.stdin.readline().strip().split())

    sub_list = num_list[N1-1:N2][::-1]

    num_list[N1-1:N2] = sub_list

for i in num_list:
    print(i, end=' ')