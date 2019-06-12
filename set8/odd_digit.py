a2 = input()
l=[]
for i in range(0,len(a2)):
    if int(a2[i])%2 !=0:
        l.append(a2[i])
print(' '.join(map(str,l)))
