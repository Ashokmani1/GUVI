p1,a1=map(int,input().split())
k=[(i,j) for i in range(p1) for j in range(p1) if i+j==(p1/2) and i*j==a1]
if len(k)>0:
    print("yes",end='')
else:
    print("no",end='')    
