n=int(input())
lo1=[1000,500,100,50,10,1]
sb=[]
c=0
for i in range(0,len(lo1)):
        k=n//lo1[i]
        c=c+k
        n=n-(k*lo1[i])
print(c)
