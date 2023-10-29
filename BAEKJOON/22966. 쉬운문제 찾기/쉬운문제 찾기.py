"""
import sys

A = int(sys.stdin.readline().strip())

caption = None
difficult = 5

for _ in range (A):
    N, K = sys.stdin.readline().strip().split()

    if int(K)<difficult:
        difficult = int(K)
        
        caption = N

print(caption)
"""

"""

n=int(input())
tmp=[]
for i in range(n):
    tmp.append(input().split())
tmp=sorted(tmp,key= lambda  x:x[1]) (문제이름부터 문제난이도 까지 [0]~[1] 뜻)
print(tmp[0][0])

"""
