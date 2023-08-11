time = int(input())

A = time//300
B = time%300//60
C = time%300%60//10
final = time%300%60%10


if final == 0:
    print(A, B, C)


elif final != 0:
    print(-1)


"""
time = int(input())
if time % 10 == 0:
    A = time // 300
    B = (time - A * 300) // 60
    C = (time - A * 300 - B * 60) // 10
    print(A, B, C)
else:
    print(-1)


"""