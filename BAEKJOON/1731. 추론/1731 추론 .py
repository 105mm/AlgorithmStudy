import sys

N1 = int(sys.stdin.readline().strip())

list_rule = []

for _ in range (N1):
    N = int(sys.stdin.readline().strip())
    list_rule.append(N)

if list_rule[0]-list_rule[1] == list_rule[1]-list_rule[2]:
    print(list_rule[-1]+list_rule[1]-list_rule[0])

else:
    print(list_rule[-1] + (list_rule[N1-1]-list_rule[N1-2])*(list_rule[2]-list_rule[1])//(list_rule[1]-list_rule[0]))




"""

n = [int(input()) for _ in range(int(input()))]

if n[0] + n[2] == n[1] * 2:
    print(n[-1] + (n[1] - n[0]))
else:
    print(n[-1] * (n[1] // n[0]))

"""