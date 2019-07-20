N1=int(input())
l=[]
for i in range(N1):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
m=sum(l)/(N1*N1)
print("%.6f" %m)
