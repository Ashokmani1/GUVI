a1=input()
b1=input()
c1=['1:']
d=['2:']
if a1.isnumeric()==False:
    a1=a1.split()
    b1=b1.split()
    for i in a1:
        if i not in b1:
            d.append(i)
    for i in b1:
        if i not in a1:
            c1.append(i)
else:
    a1=list(a1)
    b1=list(b1)
    for i in range(0,max(len(a1),len(b1))):
        if i<min(len(a1),len(b1)) and a1[i]!=b1[i]:
            d.append(a1[i])
            c1.append(b1[i])
        elif i>=min(len(a1),len(b1)):
            if max(len(a1),len(b1))==len(a1):
                d.append(a1[i])
            if max(len(a1),len(b1))==len(b1):
                c1.append(b1[i])
if len(c1)>1:
    print(*c1,sep='')
if len(d)>1:
    print(*d,sep='')
