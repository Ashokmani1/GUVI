k1=int(input())
z=0
l=[int(k1) for k1 in input().split()]
for i in range(0,len(l)):
    if l.count(l[i])>z:
        z=l.count(l[i])
        x=l[i]
print(x)
