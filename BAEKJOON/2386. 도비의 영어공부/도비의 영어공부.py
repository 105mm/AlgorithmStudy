while True:
    count = -1
    user_input = input()
    
    check = user_input[0]
    check_upper = check.swapcase()

    if user_input == '#':
        break

    for char in user_input:
        if char == check or char == check_upper:
            count += 1
    
    print (check, count)


"""
    
import sys
input = sys.stdin.readline

while True:
    q = input()
    if q[0] == '#':
        break
    q = q.lower()
    print(q[0], q[2:].count(q[0]))
    
    
"""