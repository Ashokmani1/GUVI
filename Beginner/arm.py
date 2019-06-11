def arm(s):
  a2=str(s)
  x=0
  for i in range(len(a2)):
    x=x+int(a2[i])**3
  if x == s:
    return True
  else:
    return False
  
a=int(input())
if arm(a):
  print("yes")
else:
  print("no")
