import sys

ball = 1

a = int(input())

for _ in range(a):
    N, K = map(int, sys.stdin.readline().strip().split())

    if N == ball:
        ball = K
    elif K == ball:
        ball = N
    
    else:
        pass

print(ball)

"""

def ball(num1, num2):
    a = result.index(num1)
    b = result.index(num2)
    result[a], result[b] = result[b], result[a]

m = int(input())
result = [1, 2, 3]
for _ in range(m):
    a, b = list(map(int, input().split()))
    ball(a, b)

print(result[0])


"""