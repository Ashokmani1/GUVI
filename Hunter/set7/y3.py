ba1=int(input())
bs1=[int(x) for x in input().split()]
rb1=[]
for i in range(len(bs1)-1):
	l=bs1[i+1::]
	m=max(l)
	rb1.append(m)
rb1.append(0)
print(*rb1)
