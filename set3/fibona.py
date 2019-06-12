a3=[]
a3.append(1)
a3.append(1)
a4=int(input())
if a4 <3:
  print(a3[0])
else:
  for i in range(2,a4):
    a3.append(a3[i-1] + a3[i-2])
for i in range(0,len(a3)):
  print(a3[i],end=' ')
