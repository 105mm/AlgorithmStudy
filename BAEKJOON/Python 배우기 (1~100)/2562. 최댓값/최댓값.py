import sys

list_number = []

for _ in range (9):
    a = int(sys.stdin.readline().strip())
    
    list_number.append(a)

max_value = max(list_number)
max_index = list_number.index(max_value) + 1

print(max_value)
print(max_index)
