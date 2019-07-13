n1=list(map(str,input()))
f1=[]
s=0
for i in range(len(n1)):
    if n1[i]!=" " and n1[i] not in f1:
        if s<n1.count(n1[i]):
            s=n1.count(n1[i])
            f1=[n1[i]]
        elif s==n1.count(n1[i]):
            f1.append(n1[i])
k="".join(f1)
print(s,end=" ")
print(k)
