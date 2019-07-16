a=int(input())
lis1=list(map(int,input().split()))
i=0
while(i<=len(lis1)-1):
    if i%2==0:
        if lis1[i]%2!=0:
            print(lis1[i],end=" ")
    else:
        if lis1[i]%2==0:
            print(lis1[i],end=" ")
    i+=1
