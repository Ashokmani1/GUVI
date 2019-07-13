n1=int(input())
l2=[int(i) for i in input().split()]
l1=sorted(l2)
for i in l1:
    print(l2.index(i)+1,end=" ")
