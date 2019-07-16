ab=int(input())
cd=list(map(int,input().split()))
g1=[]
for i in cd:
  if(cd.count(i)<2):
    if i not in g1:
      g1.append(i)
print(*g1)
