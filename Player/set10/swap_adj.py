a1 = int(input())
a2 = list(map(int,input().split()))
if len(a2) % 2 ==0:
    for i in range(0,len(a2),2):
        print(a2[i+1],a2[i],end=' ')
else:
    for i in range(0,len(a2)-2,2):
        print(a2[i+1],a2[i],end=' ')
    print(a2[len(a2)-1])
        
