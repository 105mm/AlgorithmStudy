import sys

N1 = int(sys.stdin.readline().strip())

list_1 = [int(N) for N in str(N1)]
list_result = []

for i in range(5):
    a = list_1[i]
    for j in range(4):
        list_1[i] *= a

print(sum(list_1))

"""

n = input()
sum = 0
for char in n:
    num = int(char)
    sum += num**(5)
print(sum)



"""