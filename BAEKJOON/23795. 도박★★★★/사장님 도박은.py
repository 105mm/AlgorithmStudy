import sys

N1 = 0
result = 0

while N1 != -1:
    N1 = int(sys.stdin.readline().strip())
    if N1 != -1:
        result += N1

print (result)


"""
s = 0
while 1:
    n = int(input())
    if n+1: s+=n
    else:
        print(s)
        break

"""