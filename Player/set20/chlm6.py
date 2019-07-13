p1=int(input())
q1=list(map(int,input().split()))
r1=sorted(q1)
print(q1.index(r1[len(r1)-1])-q1.index(r1[0]))
