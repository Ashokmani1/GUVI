nn1=int(input())

l1=list(map(int,input().split()))

l2=[]

for i in range(0,nn1):

    l2.append(l1[i])
    
    print(min(l2),end=" ")
