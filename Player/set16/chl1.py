s1=input()
l2=[]
count=0
for i in range(len(s1)):
  l2.append(s1[i])
for i in range(len(l2)):
  if(l2[i]=='a' or l2[i]=='b'):
    count+=1
if(count>=len(l2)-1):
  print("yes")
else:
  print("no")
