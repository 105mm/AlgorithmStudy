import sys

result = 0

a = []

for _ in range (4):
    minus, plus = map(int, sys.stdin.readline().strip().split())
    result -= minus
    result += plus
    a.append(result)

print(max(a))

"""
total = 0
max = 0
for _ in range(4):
    a, b = map(int, input().split())
    total = total-a+b
    if total > max:
        max = total

print(max)
"""