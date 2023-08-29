a = int(input())

for _ in range(a):
    b = int(input())
    sumhak = 0
    sumjum = 0
    for _ in range(b):
        hak, jum = map(float, input().split())
        sumhak += hak
        sumjum += hak * jum
    print(int(sumhak), f"{sumjum/sumhak:.1f}")