import sys

new_list = [0, 0, 0]

number = list(map(int, sys.stdin.readline().strip().split()))

char_list = list(sys.stdin.readline().strip())

number.sort()

A = char_list.index('A')
B = char_list.index('B')
C = char_list.index('C')

new_list[A] = number[0]
new_list[B] = number[1]
new_list[C] = number[2]

print(*new_list)

"""

print(' '.join(map(str, my_list)))

"""


"""

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
order = input()

a, b, c = sorted((a, b, c))

for i in order:
    if(i == "A"):
        print(a, end=" ")
    elif(i == "B"):
        print(b, end=" ")
    elif(i == "C"):
        print(c, end=" ")    

"""