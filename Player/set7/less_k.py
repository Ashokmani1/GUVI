a1  = list(map(int,input().split()))
a2  = list(map(int,input().split()))
a2.sort()
for i in a2:
	if i < a1[1]:
		print(i,end=' ')
