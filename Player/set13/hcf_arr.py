def hcf(x,y):
  if x < y:
    s = x
  else:
    s = y 
  for i in range(1,s+1):
    if (x % i == 0) and ( y % i ==0):
      hcf = i
  return hcf

a1 =  int(input())
a2 = list(map(int,input().split()))
x=a2[0]
for i in range(1,len(a2)):
  x=hcf(x,a2[i])
print(x)
