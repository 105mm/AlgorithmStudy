array = []
for i in range(9):
    array.append(int(input()))

array.sort()

sum_ = sum(array)

# 모두다 더하고 2명을 빼서 값이 100이라면 2개 뺀 나머지 값 출력
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if sum_ - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()


"""

https://ji-gwang.tistory.com/244


"""