a1=[]
a1.append(1)
a1.append(1)
a2=int(input())
if a2 <3:
  print(a1[0])
else:
  for i in range(2,a2):
    a1.append(a1[i-1] + a1[i-2])
for i in range(0,len(a1)):
  print(a1[i],end=' ')
