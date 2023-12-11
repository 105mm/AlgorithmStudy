import sys

forward = None
reverse = None

while True:
    fal = list(map(int, sys.stdin.readline().strip()))
    if fal == [0]:
        break
    forward = ''.join(map(str, fal))
    reverse = ''.join(map(str, fal[::-1]))
    
    if forward == reverse:
        print("yes")
    else:
        print("no")