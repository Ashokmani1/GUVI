s1=input()
s2=input()
T1=""
r=[]
n=0
for i in range(len(s1)-1):
	for j in range(i,len(s1)):
		if s1[i:j+1] in s2:
			if len(s1[i:j+1])>=len(T1):
				T1=s1[i:j+1]
				a,b=i,j
print(s1[a:b+1])
