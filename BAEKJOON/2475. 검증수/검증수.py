import sys

list_number = []

input_str = input()
input_numbers = input_str.split()

for num in input_numbers:
    list_number.append(int(num) ** 2)

print(sum(list_number) % 10)