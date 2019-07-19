nn1,kk1=map(int,input().split())
l1=[str(x) for x in input().split()]
kk1=str(kk1)
a1=" "
while kk1 in l1:
    l1.remove(kk1)
if len(l1)!=0:
    print(a1.join(l1))
else:
    print("empty")
