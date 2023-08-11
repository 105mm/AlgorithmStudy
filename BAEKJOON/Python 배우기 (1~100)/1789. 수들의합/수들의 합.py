num = input()
i = 0
cal = 0

while cal <= int(num):
    i += 1
    cal += i
    print(cal)

print(i-1)

# 마지막 합은 생각할 필요가 없다. 어차피 무슨 수 로든 채울 수 있으니까






'''가우스공식

a = int(input())

n = 1
while n * (n + 1) / 2 <= a:
    n += 1

max_n = n - 1
print(max_n)

'''