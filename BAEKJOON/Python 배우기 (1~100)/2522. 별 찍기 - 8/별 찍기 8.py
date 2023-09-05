a=int(input())


for i in range(a):
    print("*"*(i+1) + " "*(2*(a-i)-2) + "*"*(i+1))

    if i == (a-1):
        for j in range (a-1, 0, -1):
            print("*"*j + " "*2*(a-j) + "*"*j)


"""

n = int(input())
for i in range(1, n):
    print('*'*i + ' '*2*(n-i) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*2*(n-i) + '*'*i)

"""