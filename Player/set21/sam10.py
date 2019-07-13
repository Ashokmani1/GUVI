s1=input()
for i in range(0,len(s1)):
	if s1[i]<="9" or s1[i]<="F":
		a=0
	else:
		a=1
		break
if a==0:
	print("yes")
else:
	print("no")
