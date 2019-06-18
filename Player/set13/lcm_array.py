def lcm(x,y):
  if x>y:
    g = x
  else:
    g=y
  while (True):
    if (g % x == 0) and (g % y ==0):
      lcm = g
      break
    g=g+1
  return lcm
  
a1 =  int(input())
a2 = list(map(int,input().split()))
x=a2[0]
for i in range(1,len(a2)):
  x=lcm(x,a2[i])
print(x)
