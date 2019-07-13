n=int(input())
l=[int(i) for i in input().split()]
r1=[]
for i in range(len(l)-1):
    if(l[i]>l[i+1]):
        r1.append(l[i])
    else:
        r1.append(l[i+1])
s1=0
for i in range(len(r1)):
    s1=s1+r1[i]
print(s1)
