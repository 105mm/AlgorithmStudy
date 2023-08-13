now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

now_time = 3600*now[0] + 60*now[1] + now[2]
start_time = 3600*start[0] + 60*start[1] + start[2]

eta = start_time - now_time

if eta > 0:
    eta_list = [eta // 3600, (eta % 3600) // 60, eta % 60]

    for i in range(len(eta_list)):
        if eta_list[i] < 10:
            eta_list[i] = f'0{eta_list[i]}'

    print(f"{eta_list[0]}:{eta_list[1]}:{eta_list[2]}")

if eta < 0:
    eta = 86400 + eta
    eta_list = [eta // 3600, (eta % 3600) // 60, eta % 60]

    for i in range(len(eta_list)):
        if eta_list[i] < 10:
            eta_list[i] = f'0{eta_list[i]}'

    print(f"{eta_list[0]}:{eta_list[1]}:{eta_list[2]}")

if eta == 0:
    print("00:00:00")



"""
h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
t = h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1)

if t < 0 :
    t += 60 * 60 * 24

h = t // 3600
m = (t % 3600) // 60
s = t % 60

print("%02d:%02d:%02d" % (h,m,s))

"""