numbers = set()
for _ in range(28):
    numbers.add(int(input()))

all_numbers = set(range(1, 31))

missing_numbers = list(all_numbers - numbers)
missing_numbers.sort()

print(missing_numbers[0])

print(missing_numbers[1])


"""

li = [0 for i in range(1,32)]
for i in range(28):
    tmp = int(input())
    li[tmp]=1
for i in range(1,31):
    if li[i]==0:
        print(i,end=' ')
        

"""