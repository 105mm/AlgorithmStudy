import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

A, B, C = map(int, sys.stdin.readline().strip().split())

if B > b or (B == b and C >= c):
    print(A-a) #만 나이

else:
    print(A-a-1) #만 나이



print(A-a+1) #셈 나이
print(A-a) #연 나이