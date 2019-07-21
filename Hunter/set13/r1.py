p=input()
q1= 0
for i in range(0,len(p)-1):
  for j in range(i+1,len(p)):
    l=p[i:j+1]
    if l==l[::-1]:
      if len(l) > q1:
        q1 = len(l)
        k=l
print(k)
