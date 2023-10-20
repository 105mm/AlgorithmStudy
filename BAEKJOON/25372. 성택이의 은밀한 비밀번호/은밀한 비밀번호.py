import sys

N1 = int(sys.stdin.readline().strip())

for _ in range (N1):
    S = sys.stdin.readline().strip()
    if 6 <= len((str(S))) <= 9:
        print ("yes")
    else:
        print ("no")