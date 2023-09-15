import sys

n = int(sys.stdin.readline().strip())

for i in range (1,n+1):
    if i%2 != 0:
        print("* "*n)
    if i%2 == 0:
        print(" " + "* " * n)