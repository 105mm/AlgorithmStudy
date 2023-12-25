import sys

N = int(sys.stdin.readline().strip())

for _ in range (N):
    hero = sys.stdin.readline().strip()
    good = 0
    baddy = 0
    for char in hero:
        if char == 'g' or char == 'G':
            good += 1
        if char == 'b' or char == 'B':
            baddy += 1
    if good > baddy:
        print(hero + " is GOOD")
    elif good < baddy:
        print(hero + " is A BADDY")
    else:
        print(hero + " is NEUTRAL")


"""

for z in[0]*int(input()):
 s=input()
 S=s.upper().count
 c=S('G')-S('B')
 print(s,'is',('NEUTRAL','A BADDY','GOOD')[(c<0)-(c>0)])


"""