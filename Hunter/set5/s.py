n1=int(input())

l=list(map(int,input().split()))

c1=0

for i in range(1,n1+1):

	if l.count(n1*i)>0:
  
		c1=c1+1
    
print(c1)
