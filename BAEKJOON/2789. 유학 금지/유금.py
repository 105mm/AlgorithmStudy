list_remove = ['C', 'A', 'M', 'B','R', 'I', 'D', 'G', 'E']

string = input()

list_string = list(string)

list_filtered = ''.join(char for char in list_string if char not in list_remove)

print(list_filtered)

"""

a=input()
s=''
for i in a:
    if i not in ['A','B','C','D','E','G','I','M','R']: s=s+i
print(s)

"""