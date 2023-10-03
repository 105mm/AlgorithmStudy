import sys

# 두 수 입력받기
N, K = map(int, sys.stdin.readline().strip().split())

# 비교하고 결과 출력하기
if N < K:
    print("<")
elif N > K:
    print(">")
else:
    print("==")