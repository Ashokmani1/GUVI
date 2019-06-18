a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3=  a2[0:a1[0]]
a4 = a2[a1[0]:a1[0]+a1[1]]
for i in a4:
  if a3.count(i) >= 1:
    print(i,end=' ')
