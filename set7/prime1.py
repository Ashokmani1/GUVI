import math
a2=int(input())
x=0
if a2 == 2 and a2 == 3:
  print("yes")
for i in range(2,int(math.sqrt(a2))+1):
  if a2%i==0:
    print("no")
    x=x+1
    break
if x==0:
  print("yes")
