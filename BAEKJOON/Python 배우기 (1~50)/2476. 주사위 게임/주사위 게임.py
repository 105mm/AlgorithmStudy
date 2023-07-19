i = int(input())

result = []

for _ in range (i):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        result.append(10000+a*1000)
        
    elif a == b:
        result.append(1000+a*100)
        
    elif a == c:
        result.append(1000+a*100)
        
    elif b == c:
        result.append(1000+b*100)
    
    else:
        result.append(100 * max(a,b,c))


print (max(result))