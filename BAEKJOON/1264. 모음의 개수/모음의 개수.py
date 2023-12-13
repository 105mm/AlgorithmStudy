check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    count = 0
    user_input = input()
    if user_input == '#':
        break

    for char in user_input:
        if char in check:
            count += 1
    
    print(count)