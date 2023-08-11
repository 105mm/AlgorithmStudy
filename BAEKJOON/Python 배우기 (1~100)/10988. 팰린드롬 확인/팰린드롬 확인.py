word = list(input())


reverse = []


for i in range(len(word) -1, -1, -1):
    reverse.append(word[i])

if word==reverse:
    print(1)
    
else:
    print(0)