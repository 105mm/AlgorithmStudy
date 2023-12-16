n = int(input())
li = list(map(int, input().split()))
a = 0
re = []
for i in range(n-1):
    if li[i] < li[i+1]:
        a += li[i+1] - li[i]
    else:
        re.append(a)
        a = 0
re.append(a)
"""
마지막 구간이 내리막길이 아닌 경우 리스트에 a가 추가되지 않으므로
강제적으로 리스트에 마지막 오르막길의 정보를 추가한다.
"""
print(max(re))