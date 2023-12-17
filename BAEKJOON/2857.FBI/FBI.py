fbi = []

for i in range(5):
    N = input().strip()
    if 'FBI' in N:
        fbi.append(i + 1)

if len(fbi) > 0 :
    fbi.sort()
    print(' '.join(map(str, fbi)))
else:
    print("HE GOT AWAY!")