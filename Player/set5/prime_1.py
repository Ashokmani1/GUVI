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
    
    
a1 = int(input())
if prime(a1):
    print("no")
else:
    print("yes")
