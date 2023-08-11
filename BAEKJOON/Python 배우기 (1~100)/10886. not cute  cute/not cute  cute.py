count_cute = 0
count_ncute = 0


jurdge = int(input())

for _ in range (jurdge):
    vote = int(input())
    if vote == 1:
        count_cute += 1
    if vote == 0:
        count_ncute += 1

if count_ncute > count_cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

