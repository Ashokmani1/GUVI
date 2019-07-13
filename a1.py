nn=int(input())
ln1=list(map(int,input().split()))
ln1.sort()
i=0
cn1=1
while i<len(ln1)-1:
	if ln1[i]==ln1[i+1]:
		cn1=cn1+1
		i=i+2
	else:
		i=i+1
print(cn1)
