hap = int(input())

hap_list = []

for _ in range(9):
    price = int(input())
    
    hap_list.append(price)

print(hap-sum(hap_list))


