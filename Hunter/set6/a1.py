n1=int(input())

l1=[int(i) for i in input().split()]

l2=[int(j) for j in input().split()]

a=l1.index(l1[n1-2])

b=l2.index(l1[a])

print(a-b)
