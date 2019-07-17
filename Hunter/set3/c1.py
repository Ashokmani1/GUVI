row1,col1 = map(int,input().split())
b1 = []
c1 = []
for i in range(row1):
	b1.append(list(map(int,input().split())))
for i in b1:
	if 0 in i:
		for j in range(len(i)):
			if(i[j] == 0):
				c1.append(j)
			i[j] = 0
for i in b1:
	for j in c1:
		i[j] = 0
for i in b1:
	for j in range(len(i)):
		i[j] = str(i[j])
for i in b1:
	print(' '.join(i))
  
  
