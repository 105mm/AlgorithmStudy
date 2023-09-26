import sys

hol_list = []

for i in range(7):
    n = int(sys.stdin.readline().strip())
    if n%2 != 0:
        hol_list.append(n)


if len(hol_list) > 0:
    print(sum(hol_list))
    print(min(hol_list))

if len(hol_list) < 1:
    print(-1)