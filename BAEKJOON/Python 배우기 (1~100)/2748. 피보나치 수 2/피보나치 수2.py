number = int(input())

a = [0, 1]

for i in range(2, number+1):
    a.append(a[i - 2] + a[i - 1])

if number == 0:
    print(a[0])
elif number == 1:
    print(a[1])
else:
    print(a[number])

"""
import sys

n = int(sys.stdin.readline())

F = [0, 1]
for i in range(2, n + 1):
    F.append(F[i - 2] + F[i - 1])
    
print(F[n])

"""