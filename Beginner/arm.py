def arm(s):
  s=list(s)
  x=0
  for i in range(len(s)):
    x=x+s[i]**3
  if x == s:
    return True
  else:
    return False
  
a=int(input())
if arm(a):
  print("yes")
else:
  print("no")
