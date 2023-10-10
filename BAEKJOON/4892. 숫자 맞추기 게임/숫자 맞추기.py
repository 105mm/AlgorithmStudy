import sys

T=0

while True:
    N = int(sys.stdin.readline().strip())
    
    if N == 0:
        break

    T += 1

    if N%2 == 0:
        print(str(T) + ". even " + str(int(N*3/2*3/9)))
    if N%2 == 1:
        print(str(T) + ". odd " + str(int((N*3+1)/2*3/9)))
    



"""
import sys

T = 0

while True:
    N = int(sys.stdin.readline().strip())
    
    if N == 0:
        break
    
    T += 1
    
    if N % 2 == 0:
        print(str(T) + ". 짝수 " + str(N))
    else:
        print(str(T) + ". 홀수 " + str(N))


"""