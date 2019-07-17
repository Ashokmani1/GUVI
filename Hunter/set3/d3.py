alp1=input()
a=list(map(int,alp1.split()))
k=a[1]
h1=input()

s=list(map(int,h1.split()))
flag=0
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		if s[i]+s[j]==k:
			print("YES")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("NO")
		
