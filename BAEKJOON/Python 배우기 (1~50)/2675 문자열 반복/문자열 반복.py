i = int(input())
result = []

for _ in range(i):
    repeat, sentence = input().split()
    repeat = int(repeat)

    output = ''
    for char in sentence:
        output += char * repeat

    result.append(output)

for output in result:
    print(output)



'''def copyy(li,a,b):
   li.append(''.join([k*a for k in b]))
li=[]
N=int(input())
for i in range(N):
    a,b=input().split()
    a=int(a)
    copyy(li,a,b)
print('\n'.join(li))'''