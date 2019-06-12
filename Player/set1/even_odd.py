a1=input()
if len(a1)%2 !=0:
    for i in range(0,len(a1)-2,2):
        print(a1[i+1],end='')
        print(a1[i],end='')
    print(a1[len(a1)-1],end='')
else:
    for i in range(0,len(a1),2):
        print(a1[i+1],end='')
        print(a1[i],end='')
