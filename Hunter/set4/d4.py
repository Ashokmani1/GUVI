rb1=input()
a1=0
for i in range(len(rb1)):
    if rb1[:i]==rb1[i+1:]:
        a1=0
        break
    else:
        a1=1
if a1==0:
    print("YES")
else:
    print("NO")
