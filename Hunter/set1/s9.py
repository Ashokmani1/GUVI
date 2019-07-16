a1=int(input())
l=list(map(int,input().split()[:a1]))
t=max(l)
x,y=0,0
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(abs(l[i]+l[j])<t):
            x,y=l[i],l[j]
            t=abs(x+y)
print(x,y)
