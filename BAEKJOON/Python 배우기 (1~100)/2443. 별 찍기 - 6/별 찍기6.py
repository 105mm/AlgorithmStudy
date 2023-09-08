a=int(input())


for i in range(a):
    print(" "*i + "*"*(2*(a-i)-1))

for i in range(a, a*2-1):
    print(" "*(2*a-i-2) + "*"*(2*(i-a)+3))