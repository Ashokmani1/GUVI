a1=list(input())
if len(a1)%2==0:
    a1[int(len(a1)/2)] ='*'
    a1[int(len(a1)/2)-1]='*'
else:
    a1[int(len(a1)/2)] ='*'
for i in range(0,len(a1)):
    print(a1[i],end='')
