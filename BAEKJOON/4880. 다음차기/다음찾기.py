while True:

    N1, N2, N3 = map(int, input().split())

    if N1 == 0 and N2 == 0 and N3 == 0:
        break

    if N2 - N1 == N3 - N2:
            
        print ("AP " + str(N3 + (N2 - N1)))

    elif N2 // N1 == N3 // N2:

        print ("GP " + str(N3 * (N2 // N1)))

        