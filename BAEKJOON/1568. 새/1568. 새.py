import sys

N1 = int(sys.stdin.readline().strip())

Number = 1
count = 0

while N1 != 0:
    N1 -= Number
    Number += 1
    count +=1
    if Number > N1:
        Number = 1
        
print (count)