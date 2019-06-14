a1 =input().split()
x=0
for i in a1[0]:
  if a1[1].count(i) > 0:
    print("yes")
    x=x+1
    break
if x==0:
  print("no")
