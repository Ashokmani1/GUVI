a1 = int(input())
a2 = list(map(int,input().split()))
for i in range(0,len(a2)-1):
    print(max(a2[i],a2[i+1]),end=' ')
