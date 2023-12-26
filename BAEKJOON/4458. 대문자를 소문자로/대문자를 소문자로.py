import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    S = sys.stdin.readline().strip()
    S = S[0].upper() + S[1:]
    print(S)


"""

print(input().swapcase())

"""