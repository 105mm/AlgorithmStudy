import sys

def solve():
    # 사용자로부터 입력을 받음
    a, b, c = list(map(int, sys.stdin.readline().strip().split()))

    for _ in range(c):
        if a >= b:
            b += 1
        
        elif a <= b:
            a += 1
        
    print(min(a,b)*2)


# 함수 호출
solve()