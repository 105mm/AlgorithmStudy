i = int(input())

for _ in range(i):
    number, *mars = input().split()

    result = float(number)

    if mars:
        for symbol in mars:
            if symbol == "@":
                result *= 3
            elif symbol == "%":
                result += 5
            elif symbol == "#":
                result -= 7

    print(f"{result:.2f}")




''' 다른 예시

i = int(input())

for _ in range(i):
    inputs = input().split()

    result = int(inputs[0])

    if len(inputs) > 1:
        for symbol in inputs[1:]:
            if symbol == "@":
                result *= 3
            elif symbol == "%":
                result += 5
            elif symbol == "#":
                result -= 7
    else:
        print("특수 문자를 입력해주세요.")
        continue

    print(f"{result:.2f}") '''