a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
for i in a3:
    a2.append(i)
    print(max(a2),end=' ')
