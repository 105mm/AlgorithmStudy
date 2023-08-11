i = int(input())

true = 0

for _ in range(i):
    result_list = list(str(input()))

    for result in range(len(result_list)):
        if result_list[result] == "O":
            true += 1
            result_list[result] = str(true)
        elif result_list[result] == "X":
            true = 0
            result_list[result] = str(true)

    digit_sum = sum(int(digit) for digit in result_list)
    print(digit_sum)
    
    true = 0
    digit_sum=0



"""

그냥 쉽게 푸는법....

import sys

N = int(input())

for i in range(N) :
    A = list(sys.stdin.readline())
    len_ = len(A)
    cnt = 0
    sum = 0
    for j in range(len_) :
        if A[j] == 'O' :
            cnt +=  1
            sum += cnt
        else :
            cnt = 0
    print(sum)

"""