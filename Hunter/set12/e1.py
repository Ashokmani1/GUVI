p1=int(input())
q=[]
for i in range(0,p1):
   l=list(map(int,input().split()))
   q.append(l)
s=0
for i in range(0,p1):
   for j in range(0,p1):
      if i+j==p1-1:
         s=s+q[i][j]
print(s)
