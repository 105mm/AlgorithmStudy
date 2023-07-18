x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

height=None
depth=None

if x1==x2:
    depth= abs(y1-y2)
