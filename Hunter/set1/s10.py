a,b=map(int,input().split())
l1=list(map(int,input().split()[:a]))
l2=list(map(int,input().split()[:b]))
for i in l2:
    flag=0
    if(i in l1)and(l1.count(i)==l2.count(i)):
        flag=1
if(flag==1):
    print("YES")
else:
    print("NO")
