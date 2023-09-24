import sys

n = int(sys.stdin.readline().strip())

pb_list = [0,1]

for i in range(2, n+1):
    pb_list.append(pb_list[i-2]+pb_list[i-1])

print (pb_list[n])



"""
다른사람 코드

import sys
input = sys.stdin.readline

n = int(input())

def fib1(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib2(n))

"""