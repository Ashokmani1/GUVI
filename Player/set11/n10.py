n=int(input())
n1=input().split()
l1=[]
l2=[]
c1=0
for i in n1:
    l1.append(i)
e=[]
e.append(l1[0])
c1=int(l1[0])
for j in range(0,n-1):
    c1=c1+int(l1[j+1])
    e.append(c1)
print(*e,sep=' ')
    
