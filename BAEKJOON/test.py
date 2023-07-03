h,m,s = map(int, input().split())
t=3600*h+60*m+s+int(input())
H = t // 3600
M = t // 60 - 60 * H
S = t - 3600 * H - 60 * M
print(H % 24, M, S)

