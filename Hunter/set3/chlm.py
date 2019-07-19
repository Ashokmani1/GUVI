n=int(input())
l=list(map(int,input().split()))
a1=[]
for i in range(n):
    b=l[i:]
    a1.append(sum(b))
print(max(a1))
