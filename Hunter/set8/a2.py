s1=input()
if s1[-1]==".":
    s1=s1[:-1]
L=list(s1.split())
m=[]
for i in range(len(L)):
    if i%2==0:
        c=L[i]
        m.append(c[::-1])
    else:
        m.append(L[i])
print(*m)
