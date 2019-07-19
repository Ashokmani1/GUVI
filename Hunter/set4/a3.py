a1=int(input())
b=list(map(int,input().split()))
c1=b
d1=[]
while(len(c1)!=1):
    for j in range(len(c1)):
        if j%2!=0:
            d1.append(c1[j])
    c1=d1
    d1=[]
print(b.index(c1[0]))
