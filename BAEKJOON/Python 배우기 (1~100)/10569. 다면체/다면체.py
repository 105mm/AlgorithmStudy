import sys

a = int(sys.stdin.readline().strip())

for i in range (a):
    b,c = map(int, sys.stdin.readline().strip().split())

    print (abs(b-c)+2)