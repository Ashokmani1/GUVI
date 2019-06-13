a1 = input().split()
x=0
for i in range(0,len(a1[0])-len(a1[1])+1):
    if a1[0][0+i:len(a1[1])+i] == a1[1]:
        print("yes")
        x=x+1
        break
if x==0:
    print("no")
