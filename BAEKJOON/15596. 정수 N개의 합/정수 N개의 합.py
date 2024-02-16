"""
def solve(a):
    result = 0
    for i in a:
        result += i
    return result
"""

"""
def solve(a):
    return sum(a)
"""

import sys

def solve():
    # 사용자로부터 입력을 받음
    input_str = list(map(int, sys.stdin.readline().strip().split()))
    
    result = 0
    for i in input_str:
        result += i
    
    # 결과 출력tk
    print("리스트의 합:", result)

# 함수 호출
solve()