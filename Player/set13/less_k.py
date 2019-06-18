
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 =list(set(a2))
a3.sort()
for i in a3:
  if i < a1[1]:
    print(i,end=' ')
