import sys

T = int(sys.stdin.readline().strip())

result = []

for _ in range (T):
    N = int(sys.stdin.readline().strip())
    
    for i in range (1, N):
        for j in range (i+1, N):
            if i+j == N:
                if i!=j:
                    result.append((i, j))
    result_str = ", ".join(f"{pair[0]} {pair[1]}" for pair in result)
    print("Pairs for " + str(N) + ": " + str(result_str))
    result = []