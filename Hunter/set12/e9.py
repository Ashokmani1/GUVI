N=int(input())
l1=list(map(int,input().split()))
c=0
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]:
            c=c+1
print(c)
