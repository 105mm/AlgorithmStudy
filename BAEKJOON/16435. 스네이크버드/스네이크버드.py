import sys

i = 0

a, b = map(int, sys.stdin.readline().strip().split())

fruit = list(map(int, sys.stdin.readline().strip().split()))

fruit.sort()

if fruit[0] > b:
    print(b)

else:
    while True:
        b += 1
        i += 1

        if i == len(fruit) or b < fruit[i]:
            break

    print(b)


"""
N, first_h = map(int, input().split())
h_list = list(map(int, input().split()))

h_list.sort()
for h in h_list:
    if h <= first_h:
        first_h += 1
print(first_h)

"""