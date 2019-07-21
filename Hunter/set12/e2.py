p1=input()
q=input()
r=[]
for i in range(0,len(p1)):
    for j in range(0,len(q)):
        if p1[i]==q[j] and j<=i:
            if p1[i] not in r:
                r.append(p1[i])
print(''.join(list(r)))
