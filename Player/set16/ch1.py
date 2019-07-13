n1,k=map(str,input().split())
n1=list(n1)
k=int(k)
x="a"
for i in range(k-1,len(n1),k):
    x=str(n1[i])
    n1[i]=x.upper()
for i in range(0,len(n1)): print(n1[i],end="")
