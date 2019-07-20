jk=int(input())
SUM1=0
lm=str(jk)
h=[]
for i in range(0,len(lm)):
    SUM1=SUM1+int(lm[i])
    h.append(SUM1)
print(sum(h))
