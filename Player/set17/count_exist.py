a1= list(map(int,input().split()))
a2 = list(map(int,input().split()))
if a2.count(a1[1]) > 0:
  print(a1[1])
else:
  print(min(a2))
