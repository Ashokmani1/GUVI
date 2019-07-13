k=int(input())
a1=list(map(int,input().split()))
b1=[]
for i in range(1):
    for j in range(i,k):
        b.append(str(sum(a1[:j+1])))
b1=b1[::-1]
print(" ".join(b1))
