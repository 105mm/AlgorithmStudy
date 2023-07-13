N = 5

list1 = []

for _ in range(N):
    list1.append(int(input()))

for i in range(len(list1)):
    if list1[i] < 40:
        list1[i] = 40


print (sum(list1[0:])//5)