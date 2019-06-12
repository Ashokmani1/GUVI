a1=input()
x=0
for i in range(0,len(a1)):
    if a1[i].isdigit():
        print(a1[i],end='')
        x=x+1
if x==0:
    print("",end='')
