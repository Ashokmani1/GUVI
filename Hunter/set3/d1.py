n = int(input())
l = list(map(int,input().split()))
p1 = []
for i in range(len(l)):
	m = 1
	for j in range(len(l)):
		if(i == j):
			continue
		else:
			m = m * l[j]
	p1.append(str(m))
print(' '.join(p1))
