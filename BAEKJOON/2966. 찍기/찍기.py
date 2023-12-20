import sys

sang = ['A', 'B', 'C']
chang = ['B', 'A', 'B', 'C']
hyun = ['C', 'C', 'A', 'A', 'B', 'B']

name = ['Adrian', 'Bruno', 'Goran']
A, B, C = 0, 0, 0

N = int(sys.stdin.readline().strip())
Q = list(input().strip())

for i in range(N):
    if Q[i] == sang[i%3]:
        A += 1
    if Q[i] == chang[i%4]:
        B += 1
    if Q[i] == hyun[i%6]:
        C += 1

m = max(A, B, C)
print(m)
if m == A:
    print('Adrian')
if m == B:
    print('Bruno')
if m == C:
    print('Goran')