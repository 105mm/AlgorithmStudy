import sys

N, K = map(int, sys.stdin.readline().strip().split())
field = [[0] * N for _ in range(N)]


for _ in range (K):
    row, col = map(int, sys.stdin.readline().strip().split())
    field[row-1][col-1] = 1

row_runs = sum(1 for row in field if sum(row) == 0)

# 각 열을 따라 주울 때 필요한 달리기 횟수 계산
col_runs = sum(1 for col in zip(*field) if sum(col) == 0)

# 최소 달리기 횟수 출력
print(min(row_runs, col_runs))