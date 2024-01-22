import sys

count = 1

while True:
    
    N1, N2, N3 = map(int, sys.stdin.readline().strip().split())

    if N1 == 0 and N2 == 0 and N3 == 0:
        break

    if count > 1 :
        print()

    if N1 == -1:
        N1 = (N3 ** 2 - N2 ** 2) ** 0.5
        N1_result = "{:.3f}".format(N1)
        
        if abs(N1) >= N3 or N2 >= N3:
            print("Triangle #" + str(count))
            print("Impossible.")
        else:
            print("Triangle #" + str(count))
            print("a = " + N1_result)

    elif N2 == -1:
        N2 = (N3 ** 2 - N1 ** 2) ** 0.5
        N2_result = "{:.3f}".format(N2)
        
        if abs(N2) >= N3 or N1 >= N3:
            print("Triangle #" + str(count))
            print("Impossible.")
        else:
            print("Triangle #" + str(count))
            print("b = " + N2_result)

    elif N3 == -1:
        N3 = (N1 ** 2 + N2 ** 2) ** 0.5
        N3_result = "{:.3f}".format(N3)
        
        if abs(N3) <= N1 or abs(N3) <= N2:
            print("Triangle #" + str(count))
            print("Impossible.")
        else:
            print("Triangle #" + str(count))
            print("c = " + N3_result)
    
    count += 1
