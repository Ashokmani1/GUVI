n2=int(input())
l1=[int(i) for i in input().split()]
s1=0
r2=[]
for i in l1:
    s1=s1+i
    r2.append(s1)
r2=r2[::-1]
print(sep=" ",*r2)
