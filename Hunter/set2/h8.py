a1=int(input())
b1=list(map(int,input().split()))
c1=[]
for i in range(0,a1):
    d=b1[i:]
    e=max(d)
    if b1[i]==e:
        c1.append(b1[i])
print(*c1)
print(max(b1))
