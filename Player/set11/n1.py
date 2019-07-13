n1=int(input())
l1=[int(i) for i in input().split()]
s=0
for i in range(n1-1):
    s=s+(l1[i]+l1[i+1])
print(s)
