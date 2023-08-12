data = []


i = int(input())

for _ in range(i):
    name, date, month, year = input().split()
    data.append((int(year), int(month), int(date), name))


sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))


print(sorted_data[-1][3])
print(sorted_data[0][3])


"""
n = int(input())
arr = []
for _ in range(n):
    name, day, month, year = map(str, input().split())
    day = int(day)
    month = int(month)
    year = int(year)
    arr.append((year, month, day, name))
arr.sort()
print(arr[-1][3])
print(arr[0][3])


"""