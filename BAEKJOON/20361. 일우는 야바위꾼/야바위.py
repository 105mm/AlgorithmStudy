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


"""

N, X, K = map(int, input().split())
Shell = [0] * (N + 1)
Shell[X] = 1

for _ in range(K):
    A, B = map(int, input().split())
    Shell[A], Shell[B] = Shell[B], Shell[A]
    
print(Shell.index(1))

"""