import math
a1=int(input())
x=0
if a1 == 2 and a1 == 3:
  print("yes")
for i in range(2,int(math.sqrt(a1))+1):
  if a1%i==0:
    print("no")
    x=x+1
    break
if x==0:
  print("yes")
