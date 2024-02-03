two_dimensional_array = []

for _ in range(9):
    row_input = input()
    row = list(map(int, row_input.split()))
    two_dimensional_array.append(row)


max_value = float('-inf')
max_row = 0
max_col = 0

for i, row in enumerate(two_dimensional_array):
    for j, value in enumerate(row):
        if value > max_value:
            max_value = value
            max_row = i
            max_col = j

print(max_value)









print(max_row + 1, max_col + 1)


"""

result, ii, jj = 0, 0, 0

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] > result:
            result = board[i][j]
            ii, jj = i, j

print(result)
print(ii + 1, jj + 1)



"""