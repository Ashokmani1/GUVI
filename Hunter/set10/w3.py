from itertools import permutations
s1=input()
kk=permutations(s1)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==s1:
  print(s1)
elif s1==a[::-1]:
  print("-1")
else:
	s1=tuple(s1)
	for i in kk:
		l.append(i)
	for i in l:
		if i>s1:
			m=i
			break

	for i in l:
		if i>s1 and i<m:
			m=i

	if m==-1:
		print("-1")
	else:
		for i in m:
			print(i,end="")
