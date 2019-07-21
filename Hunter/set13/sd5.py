k1=int(input())
lis1=list(map(int,input().split()))
u=sorted(lis1)
v=u[::-1]
e=[]
for i in range(0,len(lis1)):
  e.append(v[i])
  e.append(u[i])
for j in e[:len(lis1)]:
  print(j,end=" ")
