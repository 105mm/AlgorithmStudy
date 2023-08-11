time = int(input())

A = 100
B = 100


for _ in range (time):
    a, b = map(int, input().split())

    if a>b:
        B -=a
    
    if a<b:
        
        A -=b
    
    if a==b:

        pass


print (A)
print (B)


"""
n = int(input())
x = y = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        y -= a
    elif a < b:
        x -= b
        
print(x, y, sep = "\n")

"""