n=list(map(str,input()))
d1=[]
i=0
while i<(len(n)):
    d1.append(n[i])
    d1.append(str(n.count(n[i])))
    i=i+(n.count(n[i]))
s="".join(d1)
print(s)
