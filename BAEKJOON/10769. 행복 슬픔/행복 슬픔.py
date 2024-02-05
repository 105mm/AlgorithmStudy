import sys

a = sys.stdin.readline().strip()

if a.count(":-)") == 0 and a.count(":-(") == 0:
    print("none")
elif a.count(":-)") == a.count(":-("):
    print("unsure")
elif a.count(":-)") > a.count(":-("):
    print("happy")
else:
    print("sad")