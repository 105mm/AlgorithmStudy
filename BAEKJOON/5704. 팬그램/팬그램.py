alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

while True:
    
    user_input = input()

    if user_input == '*':
        break


    
    for char in user_input:
        if char in alphabet_set:
            alphabet_set.remove(char)

    
    if not alphabet_set:
        print('Y')
    else:
        print('N')

    
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")