n1,n2=map(int,input().split())

l1=[str(i) for i in input().split()]

a=l1[n2:]+l1[:n2]

print(' '.join(a))
