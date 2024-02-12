import sys

J = list(map(int, sys.stdin.readline().strip().split()))
S = list(map(int, sys.stdin.readline().strip().split()))

JS = 0
SS = 0

yuk = 0

for i in range (9):

    JS += J[i]
    if JS > SS:
        yuk = 1
    SS += S[i]


if yuk == 1 and sum(J) < sum(S):
    print("Yes")

else:
    print("No")