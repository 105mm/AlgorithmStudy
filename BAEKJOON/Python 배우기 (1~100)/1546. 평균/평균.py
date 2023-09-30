import sys

num = int(sys.stdin.readline().strip())

a = list(map(int, sys.stdin.readline().strip().split()[:num]))

lie_a = []

for i in a:
    lie_a.append(i/max(a)*100)

print(sum(lie_a)/len(lie_a))