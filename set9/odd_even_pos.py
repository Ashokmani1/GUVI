a2=input()
l=[]
l1=[]
for i in range(0,len(a2),2):
    l.append(a2[i])

for i in range(1,len(a2),2):
    l1.append(a2[i])
print(''.join(map(str,l)),''.join(map(str,l1)))
