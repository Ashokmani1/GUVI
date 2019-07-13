n=int(input())
a=list(map(int,input().split()))[:n]
b1=set(a)
print(*b1,end="")
