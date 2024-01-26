import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N1, N2 = map(int, sys.stdin.readline().strip().split())

    cnt = 0

    for _ in range(N1):

        M1, M2, M3 = map(int, sys.stdin.readline().strip().split())


        if ((M1 * M2) / M3) >= N2:
            
            cnt += 1
        
    print(cnt)