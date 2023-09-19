import sys

a = int(input())
b = int(input())

list_prime = []

for i in range(a, b+1):
    is_prime = True  # 소수 판별 변수
    if i < 2:
        is_prime = False  # 2보다 작은 숫자는 소수가 아님
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False  # 소수가 아님
                break
    if is_prime:
        list_prime.append(i)


if list_prime:
    print(sum(list_prime))
    print(min(list_prime))

else:
    print(-1)





"""
처음에 짰던 코드

import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

list_prime = []


for i in range (a, b+1):
    
    for j in range (2, b+1):
        
        
        if i%j == 0:
            count += 1
        
        if count == 0:
            list_prime.append(i)


print (list_prime)

"""
"""
import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

list_prime = []


for i in range (a, b+1):
    is_prime = True
    if i < 2:
        is_prime = False
    else:
        for j in range (2, int(b**0.5)+1):
            if i%j == 0:
                is_prime = False
                break
    if is_prime:
        list_prime.append(i)

print (list_prime)

"""