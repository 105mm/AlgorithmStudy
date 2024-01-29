import sys, math

N1 = int(sys.stdin.readline().strip())

for _ in range (N1):
    M1 = int(sys.stdin.readline().strip())

    for i in range (101):
        if i+i**2 > M1:
            print(i-1)
            break