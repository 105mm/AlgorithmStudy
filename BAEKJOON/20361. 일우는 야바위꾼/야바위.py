import sys

N1, N2, N3 = map(int, sys.stdin.readline().strip().split())

cup = []

imsi = None

for i in range(1, N1+1):
    cup.append(i)

for _ in range(N3):
    M1, M2 = map(int, sys.stdin.readline().strip().split())

    imsi = cup[M1-1]
    cup[M1-1] = cup[M2-1]
    cup[M2-1] = imsi

print(cup.index(N2)+1)