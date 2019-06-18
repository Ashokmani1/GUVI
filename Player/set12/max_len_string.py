a1=input().split()
l=[]
for i in a1:
  l.append(len(i))
print(a1[l.index(max(l))])
