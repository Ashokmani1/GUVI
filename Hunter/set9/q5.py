a,b=map(int,input().split())
c1=list(map(int,input().split()))[:a]
d1=0
for i in range(len(c1)):
    if c1[i]<=b:
       d1+=1
print(d1)
