n1=int(input())
c1=0
if(n1<2):
    print("0")
else:
    for i in range(2,n1+1):
        while(i>0):
            b=i%10
            if b==2:
                c1=c1+1 
            i=i//10
    print(c1)
