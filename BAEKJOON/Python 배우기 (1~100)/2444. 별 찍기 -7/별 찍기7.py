a=int(input())


for i in range(a-1, -1, -1):
    print(" "*i + "*"*(2*(a-i)-1))

    if i == 0 :
        for j in range (1, a):
            print(" "*j + "*"*(2*(a-j)-1))