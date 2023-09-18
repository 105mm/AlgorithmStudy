import sys

a, b = map(int, sys.stdin.readline().strip().split())

list_0 = list(map(int, sys.stdin.readline().strip().split()[:a]))

for i in range (a):
    if list_0[i] < b:
        print(list_0[i], end=" ")





"""
import sys

a, b = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))
result = [str(num) for num in numbers if num < 5]

print(" ".join(result))



"""