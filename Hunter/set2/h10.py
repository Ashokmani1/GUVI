aa,b1=map(int,input().split(" "))
l1=list(map(int,input().split(" ")))
r1=[[abs(i-b1),i]for i in l1]
r1=sorted(r1)
r1=r1[1:]
r1=[i[1] for i in r1[ :3]]
print(*r1)
