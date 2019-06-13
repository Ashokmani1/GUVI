a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
for i in range(0,len(a2)):
    print(a2[(((len(a2)-a1[1])+i)%len(a2))],end=' ')
