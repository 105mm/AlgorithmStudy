import math

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    
    print(math.lcm(a,b))





'''
처음에 짠 코드


N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    c = a*b+1

    for i in range(1, c):
        if i % a == 0 and i % b == 0:
            
            print(i)

            break

            
a에 둘 중에 큰 수를 넣고
a를 b로 나누었을때 0이 아닐때까지 반복한다.
a % b 가 0 일때 while 문을 빠져나와서
a와b의 곱을 가장 마지막 나머지 수로 나누어서 최소 공배수를 구한다.

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    m = a*b
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    print(int(m/b))
            

'''