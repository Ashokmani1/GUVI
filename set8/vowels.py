a2=input()
x=0
a3=['a','e','i','o','u']
for i in range(0,len(a2)):
  if a2[i] in a3:
    print("yes")
    x=x+1
    break
if x == 0:
    print("no")
