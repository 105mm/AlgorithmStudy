N = int(input())

while True:
    M = int(input())
    if M == 0:
        break
    
    if M % N != 0:
        print(str(M) + " is NOT a multiple of " + str(N) + ".")
    else:
        print(str(M) + " is a multiple of " + str(N) + ".")

"""

N = int (input ())

while True :

    K = int (input ())

    if (K == 0) : break

    if (K % N != 0) : print (f"{K} is NOT a multiple of {N}.")
        
    if (K % N == 0) : print (f"{K} is a multiple of {N}.")


"""