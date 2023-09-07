a=int(input())



for _ in range(a):
    car_price = int(input())
    option = int(input())

    hap_op = 0

    for _ in range(option):

        op_num, op_price = map(int, input().split())

        hap_op += op_num*op_price

    print(car_price+hap_op)