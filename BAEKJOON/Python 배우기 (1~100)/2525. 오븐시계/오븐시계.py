hour,minute = map(int,input().split())
oven = int(input())

fminute=minute+oven

while fminute>=60:
    fminute -= 60
    hour += 1
    if hour>=24:
        hour = 0


print(hour,fminute)