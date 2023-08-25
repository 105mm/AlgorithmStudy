"""
import sys

a, b = map(int, sys.stdin.readline().split())

yak = 1
bae = a* b

if a>=b:
    for iy in range (1, a+1):
        if a%iy == 0 and b%iy == 0:
            yak = iy
    
    for ib in range (a, a*b+1):
        if ib%a == 0 and ib%b == 0:
            bae = ib
            break

if a<=b:
    for iy in range (1, b+1):
        if a%iy == 0 and b%iy == 0:
            yak = iy
    
    for ib in range (b, a*b+1):
        if ib%a == 0 and ib%b == 0:
            bae = ib
            break


print(yak)
print(bae)
"""
"""
import sys

a, b = map(int, sys.stdin.readline().split())

gcd_value = 1
lcm_value = a * b  # 초기값 설정

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd_value = i

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm_value = i
        break

print(gcd_value)
print(lcm_value)
"""

import sys

def yak(a, b):
    while b:
        a, b = b, a % b
    return a

def bae(a, b):
    return a * b // yak(a, b)

a, b = map(int, sys.stdin.readline().split())

gcd_value = yak(a, b)
lcm_value = bae(a, b)

print(gcd_value)
print(lcm_value)

"""
a,b = list(map(int,input().split()))

# if b >a :
#     a ,b = b,a

ori_a , ori_b = a,b

while a %b !=0:
    a,b = b, a%b

print(b )
print(ori_a *ori_b//b)
"""