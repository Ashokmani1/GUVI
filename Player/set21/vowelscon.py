a1 = input()
a2 = ['a','e','i','o','u']
a3=[]
a4=[]
for i in a1:
    if i in a2:
        a3.append(i)
    else:
        a4.append(i)
print(''.join(map(str,a3+a4)))
