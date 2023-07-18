x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

height=None
depth=None
x4=None
y4=None

if x1==x2:
    height= abs(y1-y2)
if x1==x3:
    height= abs(y1-y3)
if x2==x3:
    height= abs(y2-y3)

if y1==y2:
    depth= abs(x1-x2)
if y1==y3:
    depth= abs(x1-x3)
if y2==y3:
    depth= abs(x2-x3)

if x1==x2:
    if x1>x3:
        x4=abs(x1-depth)
    else :
        x4=x1+depth
if x1==x3:
    if x1>x2:
        x4=abs(x1-depth)
    else :
        x4=x1+depth
if x2==x3:
    if x2>x1:
        x4=abs(x2-depth)
    else :
        x4=x2+depth

if y1==y2:
    if y1>y3:
        y4=abs(y1-height)
    else:
        y4=y1+height
if y1==y3:
    if y1>y2:
        y4=abs(y1-height)
    else:
        y4=y1+height
if y2==y3:
    if y2>y1:
        y4=abs(y2-height)
    else:
        y4=y2+height        

print (x4,y4)


'''
리스트를 만들어 입력받고 리스트[i] 의 숫자의 개수를 세고
개수가 한 개밖에 없는 경우 리스트[i]를 각각 x4, y4 에 대입한다

x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)
'''