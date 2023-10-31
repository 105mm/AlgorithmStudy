import sys
import math

X, Y, R = map(int, sys.stdin.readline().strip().split())


X_1, Y_1, R_1 = map(int, sys.stdin.readline().strip().split())


if R+R_1 < math.sqrt(pow((max(X,X_1)-min(X,X_1)),2)+pow((max(Y,Y_1)-min(Y,Y_1)),2)):
    print("NO")

if R+R_1 > math.sqrt(pow((max(X,X_1)-min(X,X_1)),2)+pow((max(Y,Y_1)-min(Y,Y_1)),2)):
    print("YES")

if R+R_1 == math.sqrt(pow((max(X,X_1)-min(X,X_1)),2)+pow((max(Y,Y_1)-min(Y,Y_1)),2)):
    print("NO")



"""

X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

if (abs(X1-X2)**2+abs(Y1-Y2)**2) < (R1+R2)**2:
    print("YES")
else:
    print("NO")

"""

