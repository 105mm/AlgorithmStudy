a = None
b = None

while a !=0 or b != 0:

    a ,b = map(int, input().split())

    
    if a == 0 and b == 0:
        break
    
    if b%a == 0 and a%b != 0:
        print("factor")
    
    if a%b == 0 and b%a != 0:
        print("multiple")
    
    if a%b !=0 and b%a != 0:
        print("neither")

