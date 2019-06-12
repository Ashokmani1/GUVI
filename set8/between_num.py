a1=int(input())
a2=list(map(int,input().split()))
if a1 > a2[0] and a2[1] > a1:
  print("yes")
else:
  print("no")
