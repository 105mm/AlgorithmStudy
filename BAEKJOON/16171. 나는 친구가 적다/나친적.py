import sys

check = list(sys.stdin.readline().strip())

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

check_2 = []

for i in range(len(check)):
    if check[i] not in num:
        check_2.append(check[i])

check_2 = ''.join(check_2)

keyword = sys.stdin.readline().strip()

if keyword in check_2:
    print(1)

else:
    print(0)