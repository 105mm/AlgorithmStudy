a = int(input())

for _ in range (a):
    b = int(input())
    store = list(map(int, input().split()))[:b]

    print ((max(store)-min(store))*2)

    store = []