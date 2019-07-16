b1,sa1=map(int,input().split())
p=[]
for i in range(b1):
  s1=set(map(int,input().split()))
  p.append(s1)
ro=s1.intersection(*p)
print(*ro)
