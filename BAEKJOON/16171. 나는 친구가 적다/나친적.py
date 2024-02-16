import sys

check = list(sys.stdin.readline().strip().split())

while True:
    count = 0
    user_input = sys.stdin.readline().strip()
    if user_input == '#':
        break

    for char in user_input:
        if char in check:
            count += 1
    
    print(count)
