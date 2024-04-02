char_to_num = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}


while True:

    num = []
    x = 0
    result = 0

    user_input = input()
    
    if user_input == '#':
        break
    
    for char in user_input:
        num.append(char_to_num[char])
        
        
    for i in reversed(num):
        result += i*8**x
        x += 1
    
    
    print (result)


"""

import sys
input = sys.stdin.readline

n = "-\\(@?>&%"

while True:
    s = input().strip()[::-1]
    if s == '#':
        break

    print(sum((n.find(s[i])) * 8**i for i in range(len(s))))

"""

