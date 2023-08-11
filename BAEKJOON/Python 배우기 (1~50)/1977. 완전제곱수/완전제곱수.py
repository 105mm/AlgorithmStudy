a = int(input())
b = int(input())

p_list = []

for i in range (1, b+1):
    if a <= i*i <= b:
        p = i*i
        p_list.append(p)

if len(p_list) == 0:
    print(-1)

else:
    print (sum(p_list))
    print (min(p_list))


"""
M, N = map(int, (input() for _ in range(2)))

result = [x for x in range(M, N+1) if (x**0.5).is_integer()]
if result:
  print(f"{sum(result)}\n{min(result)}")
else:
  print(-1)

"""