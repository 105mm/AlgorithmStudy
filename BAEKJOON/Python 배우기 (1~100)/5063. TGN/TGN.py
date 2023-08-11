N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())

    if e - c > r:
        print("advertise")
    elif e - c == r:
        print("does not matter")
    else:
        print("do not advertise")


"""

e+c = 총 수익

총 수익에서 이전 금액을 빼면 어떻게 되든간에 수익권인지 손해인지 알 수 있다.

"""