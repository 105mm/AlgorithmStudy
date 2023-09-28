import sys

a = int(sys.stdin.readline().strip())

list_yut = []

bulbub = 0

list_0 = list(map(int, sys.stdin.readline().strip().split()[:5]))

for i in list_0:
    if i == a:
        bulbub += 1

print(bulbub)


"""
플레티넘 코드..

N = int(input())
s = input()
s = s.split(' ')
s = [int(x) for x in s]
print(s.count(N))


"""