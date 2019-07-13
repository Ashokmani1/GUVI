n1=int(input())
l1=[int(i) for i in input().split()]
r=[]
for i in range(len(l1)-1):
    if(l1[i]>l1[i+1]):
        r.append(l1[i])
    else:
        r.append(l1[i+1])
s=0
for i in range(len(r)):
    s=s+r[i]
print(s)
