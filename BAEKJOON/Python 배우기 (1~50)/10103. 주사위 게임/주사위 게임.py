time = int(input())

A = 100
B = 100


for _ in range (time):
    a, b = map(int, input().split())

    if a>b:
        B -= a
    
    if a<b:
        
        A -= b
    
    if a==b:

        pass


print (A)
print (B)