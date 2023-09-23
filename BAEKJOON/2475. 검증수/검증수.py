import sys

list_number = []

input_str = input()
input_numbers = input_str.split()

for num in input_numbers:
    list_number.append(int(num) ** 2)

print(sum(list_number) % 10)



"""
그냥 ㅓ이렇게 간단하게 해라

num=map(int, input().split())
sum=0
for i in num:

    sum+=i**2

print(sum%10)

"""