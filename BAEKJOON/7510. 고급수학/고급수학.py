import sys

a = int(sys.stdin.readline().strip())

count = 0

while True:
    count += 1

    N1, N2, N3 = map(int, sys.stdin.readline().strip().split())

    print("Scenario #" + str(count) + ":")

    if N1 ** 2 + N2 ** 2 == N3 ** 2 or N1 ** 2 + N3 ** 2 == N2 ** 2 or N2 ** 2 + N3 ** 2 == N1 ** 2:
        print("yes")
    else:
        print("no")

    if count == a:
        break
    else:
        print()

"""

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "yes"
    else:
        return "no"

# 입력
t = int(input())  # 테스트 케이스의 개수

for i in range(1, t+1):
    a, b, c = map(int, input().split())
    
    # 출력
    print(f"Scenario #{i}:")
    print(is_right_triangle(a, b, c))
    
    # 각 테스트 케이스 사이에 빈 줄 출력
    if i != t:
        print()

"""