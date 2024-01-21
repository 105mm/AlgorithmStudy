import sys

N = int(sys.stdin.readline().strip())

for _ in range (N):
    a = int(sys.stdin.readline().strip())
    num_list = list(range(1, a+1))

    for i in range (2, a+1):
        for j in range (1, a//i+1):
            if i*j in num_list:
                num_list.remove(i*j)
            else:
                num_list.append(i*j)
    
    print(len(num_list))