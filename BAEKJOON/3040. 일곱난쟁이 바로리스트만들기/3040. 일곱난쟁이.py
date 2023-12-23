import sys

nan = [int(sys.stdin.readline().strip()) for _ in range(9)]

for i in range (8):
    for j in range (i+1, 9):
        nan_copy = nan[:]
        nan_copy.remove(nan[i])
        nan_copy.remove(nan[j])
        if sum(nan_copy) == 100:
            for k in nan_copy:
                print (k)
            sys.exit()