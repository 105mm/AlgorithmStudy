number = float(input())

yaksu = []

if number == -1:
    break

for i in range (1, (number//2)+1):
    if number%i == 0:
        yaksu.append(i)

yaksusum = " + ".join(map(str, yaksu))

if sum(yaksu) == number:
    print(str(number) + " = " + str(yaksusum))

elif sum(yaksu) != number:
    print(str(number) + " is NOT perfect.")