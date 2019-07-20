a1=input()
b=c=0
for i in range(len(a1)):
    b=1
    for j in range(i+1,len(a1)):
        if(a1[i]==a1[j]):
            b+=1
        else:
            break
    if b>c:
        c=b
        d=a1[i]
print(d,c)
