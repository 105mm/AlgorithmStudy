import sys

N, K = map(int, sys.stdin.readline().strip().split())

if N > K:
    N, K = K, N

print(((K-N+1)*((2*N)+(K-N+1-1)))//2)


"""

등차수열의 합

N{2a+(n-1)d} // 2

N = 항의 개수 , a = 초항, d = 공차

항의 개수

(마지막 항-처음 항) // 공차 + 1


"""