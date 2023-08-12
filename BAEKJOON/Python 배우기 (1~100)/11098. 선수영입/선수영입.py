a = int(input())



for _ in range(a):

  b = int(input())
  price_list = []
  name_list = []
  
  for _ in range(b):
    price, name = input().split()
    price_list.append(int(price))
    name_list.append(name)
    
  max_price_index = price_list.index(max(price_list))
  print(name_list[max_price_index])



  """
  n = int(input())

for _ in range(n) :
    p = int(input())
    c_max = 0
    name_max = ""

    for _ in range(p) :
        c , name = input().split()
        c = int(c)

        if c > c_max :
            c_max = c
            name_max = name
    print(name_max)

  
  """