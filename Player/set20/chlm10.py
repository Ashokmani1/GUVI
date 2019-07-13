k1=str(input())
a=[]
b=""
for i in k1:
    if k1.count(i)!=1 and i not in a:
        a.append(i)
        b=b+i 
    elif k1.count(i)==1:
        b=b+i 
print(b)
