num1=list(map(str,input()))
set1=cs=0
for i in range(0,len(num1)-1):
  q1=num1[i]
  if int(q1)!=0:
   for j in range(i+1,i+2):
    q1=q1+num1[j]
    if int(q1)<27 and int(q1)>0: set1=set1+1
    elif int(q1)==0: set1=set1-1
    else: break
if set1!=1: cs=set1%2
print(set1+cs+1)
