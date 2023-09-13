import sys

a = int(sys.stdin.readline().strip())

for i in range (a):
    b,c = map(int, sys.stdin.readline().strip().split())

    print ("Case " + str(i+1) + ": " + str(b+c) )




"""
for i in[*open(n:=0)][1:]:n+=1;print("Case %d:"%n,eval('+'.join(i[:-1])))

?????????

"""