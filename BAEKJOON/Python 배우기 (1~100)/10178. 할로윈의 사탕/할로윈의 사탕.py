import sys

a = int(sys.stdin.readline().strip())

for _ in range (a):
    b, c = map(int, sys.stdin.readline().strip().split())

    print ("You get " + str(b//c) + " piece(s) and your dad gets " + str(b%c) + " piece(s).")