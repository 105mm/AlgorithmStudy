a = int(input())

remain = 0

for _ in range (a):
    stu, app = map(int, input().split())
    remain += app % stu

print (remain)