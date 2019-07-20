N1=input()
temp=""
f=0
for i in range(len(N1)):
  if N1[i]==" ":
    temp+=N1[i]
  elif f==0:
    temp+=N1[i].upper()
    f=1
  elif f==1:
    temp+=N1[i]
    f=0
print(temp)
