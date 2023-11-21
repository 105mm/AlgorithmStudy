import sys

M = int(sys.stdin.readline().strip())

result = []



for _ in range (M):

    most_numbers = []
    max_count = 0

    a,b,c,d = map(int, sys.stdin.readline().strip().split())

    numbers = [a, b, c, d]

    count_dict = {}
    
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_count = max(count_dict.values())
    most_numbers = [num for num, count in count_dict.items() if count == max_count]

    if max_count == 4:
        result.append(50000+most_numbers[0]*5000)
    if max_count == 3:
        result.append(10000+most_numbers[0]*1000)
    if max_count == 2 and len(most_numbers)==2:
        result.append(2000+most_numbers[0]*500+most_numbers[1]*500)
    elif max_count == 2:
        result.append(1000+most_numbers[0]*100)
    if max_count == 1:
        result.append(max(most_numbers)*100)


print(max(result))



"""

N = int(input())

maxPrice = 0
for _ in range(N):
    dice = list(map(int, input().split()))
    cntDice = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
    for d in dice:
        cntDice[d-1][1] += 1
        
    cntDice.sort(key=lambda x:(-x[1], -x[0]))
    
    maxDice = cntDice[0]
    secondDice = cntDice[1]
    minDice = cntDice[-1]
    
    if maxDice[1] == 4:      
        maxPrice = max(maxPrice, 50000 + maxDice[0] * 5000)
    elif maxDice[1] == 3:
        maxPrice = max(maxPrice, 10000 + maxDice[0] * 1000)
    elif maxDice[1] == 2:
        if secondDice[1] == 2:
            maxPrice = max(maxPrice, 2000 + maxDice[0] * 500 + secondDice[0] * 500)
        else:
            maxPrice = max(maxPrice, 1000 + maxDice[0] * 100)
    else:
        maxPrice = max(maxPrice, maxDice[0] * 100)

print(maxPrice)


"""