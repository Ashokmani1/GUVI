r=int(input())
l1=list(map(int,input().split()))
print((l1.index(min(l1))+1),end=" ")
print((l1.index(max(l1))+1))
