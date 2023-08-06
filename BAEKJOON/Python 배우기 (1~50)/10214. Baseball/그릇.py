a = int(input())

for _ in range(9):
    y, g = map(int, input().split())

    if y>g:
        print("Yonsei")
    if y<g:
        print("Korea")
    if y==g:
        if y!=0 and g!=0:
            print("Draw")
    if y==0 and g==0:
        pass