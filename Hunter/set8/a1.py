n1,k1=map(int,input().split())
L1=list(map(int,input().split()))
sum=[]
for i in range(n1-k1,n1):
	sum.append(str(L1[i]))
print(" ".join(sum))
