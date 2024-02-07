import sys

N = int(sys.stdin.readline().strip())

m_list = []

for _ in range (N):
    
    K = sys.stdin.readline().strip()

    m_list.append(K)

N2 = int(sys.stdin.readline().strip())

if N2 == 1:

    for i in m_list:
        print(i)

elif N2 == 2:

    for i in m_list:
        print(i[::-1])

elif N2 == 3:

    for i in reversed(m_list):
        print(i)