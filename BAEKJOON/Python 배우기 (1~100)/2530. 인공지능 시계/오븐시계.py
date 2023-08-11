hour,minute,sec= map(int,input().split())
oven = int(input())

fsec=sec+oven

while fsec>=60:
    fsec -= 60
    minute += 1
    if minute>=60:
        minute -= 60
        hour += 1
        if hour >=24:
            hour -=24
            if fsec<60:
                break

print(hour,minute,fsec)





# h,m,s = map(int, input().split())
# t=3600*h+60*m+s+int(input())
# H = t // 3600
# M = t // 60 - 60 * H
# S = t - 3600 * H - 60 * M
# print(H % 24, M, S)