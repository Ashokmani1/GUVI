X1=int(input())
l1=list(map(int,input().split()))[:X1]
for i in range(0,X1):
    if(l1[i]==0):
       l1.remove(l1[i])
       l1.append(0)
print(*l1,end="")
