a = None
b = None

while a !=0 or b != 0:


    a ,b = map(int, input().split())

    if a == 0 and b == 0:

        break
    
    
    print (a+b)