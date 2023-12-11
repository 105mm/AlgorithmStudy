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

"""
from sys import stdin

while True:
  i = stdin.readline().rstrip()
  if i == '0':
    break

  if i == i[::-1]:
    print('yes')
  else:
    print('no')


"""