p,q=list(map(str,input().split()))
l1=[]
for i in p:
    for j in q:
        if i==j:
            l1.append(i)
print("".join(l1))
