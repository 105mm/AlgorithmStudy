a=int(input())


for i in range(a, 0, -1):
    print(" "*(i-1) + "*"*((a-i)+1))

    if i == 1 :
        for j in range (1, a):
            print(" "*j + "*"*(a-j))