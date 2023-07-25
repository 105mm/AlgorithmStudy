jurdge = int(input())
vote = input()
a = list(vote[:jurdge])

count_a = 0
count_b = 0

if a:
    for grade in a:
        if grade == "A":
            count_a += 1
        elif grade == "B":
            count_b += 1

if count_a > count_b:
    print("A")
elif count_a == count_b:
    print("Tie")
else:
    print("B")