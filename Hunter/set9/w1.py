def difff(y1):
    s=0
    for i in range(0,len(y1)):
        if y1[i]=='2':
            s=s+1
    return s
n=int(input())
s=0
for i in range(0,n+1):
    y1 = list(str(i))
    s=s+difff(y1)
print(s)
