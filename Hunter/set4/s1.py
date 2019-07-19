rb1=int(input())
ar1=list(map(int,input().split()))
pro=1
res=[]
for i in range(0,len(ar1r1)):
    for j in range(i,len(ar1r1)):
        pro=pro*ar1[j]
        res.append(pro)
    pro=1
print(max(res))
