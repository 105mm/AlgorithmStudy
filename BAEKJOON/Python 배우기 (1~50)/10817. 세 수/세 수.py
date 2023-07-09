a = list(map(int, input().split()))

max_number = max(a)
second_largest = None

for number in a:
    if number != max_number:
        if second_largest is None or number > second_largest:
            second_largest = number

if second_largest is None:
    second_largest = max_number

print(second_largest)

'''


a = list(map(int, input().split()))

if len(a) >= 2:
    sorted_list = sorted(a)
    second_largest = sorted_list[-2]
    print(second_largest) 
    

    
'''