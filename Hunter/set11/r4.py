X=int(input())
Y=list(map(str,input().split()))[:X]
l1=[]
t=[]
for i in range(0,len(Y)):
    l1.append(Y[i].lower())
for i in range(0,X):
      m=min(l1)
      t.append(m)
      l1.remove(min(l1))
for i in t:
    print(i)
