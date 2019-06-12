import math
def prime(a1):
  x=0
  if a1 == 2 and a1 == 3:
    return True
  for i in range(2,int(math.sqrt(a1))+1):
    if a1%i==0:
      return False
      x=x+1
      break
  if x==0:
    return True
    
a3=list(map(int,input().split()))
a1=a3[0]
a2=a3[1]
x=0
for i in range(a1,a2+1):
  if prime(i):
    x=x+1
print(x)
