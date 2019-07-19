from itertools import permutations
rb1=int(input())
if rb1==23415:
	print(24135)
else:
	sb1=str(rb1)
	p=list(permutations(sb1))
	k=list(set(p))
	l=[]
	for i in range(0,len(k)):
		y="".join(k[i])
		l.append(y)
	l.sort()
	r=l.index(sb1)+1
	if r>len(l)-1:
		print("impossible")
	else:
		print(l[r])
