a1 =  input().split()
for i in range(0,len(a1[0])):
    a1[1] = a1[1].replace(a1[0][i],"")
if len(a1[1]) ==  int(a1[2]):
    print("yes")
else:
    print("no")
