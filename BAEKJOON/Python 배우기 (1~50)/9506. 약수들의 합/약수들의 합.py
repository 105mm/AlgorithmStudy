while True:
    number = float(input())

    if number == -1:
        break

    yaksu = []

    for i in range(1, (int(number) // 2) + 1):
        if number % i == 0:
            yaksu.append(i)

    yaksusum = " + ".join(map(str, yaksu))

    if sum(yaksu) == number:
        print(str((int(number))) + " = " + str(yaksusum))
    else:
        print(str((int(number))) + " is NOT perfect.")




"""
while True:
    sum = 0
    lst = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    for j in lst:
        sum += j
    if n == sum:
        print(f'{n} = {lst[0]}', end= '')
        for i in range(1, len(lst)):
            print(f' + {lst[i]}', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')
    

"""