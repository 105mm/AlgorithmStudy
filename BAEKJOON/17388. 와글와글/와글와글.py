import sys

list_w = list(map(int, sys.stdin.readline().strip().split()))

list_n = ["Soongsil", "Korea", "Hanyang"]

index_w = list_w.index(min(list_w))

if sum(list_w) >= 100:
    print("OK")

else:
    print(list_n[index_w])