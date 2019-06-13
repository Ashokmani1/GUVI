a1 = list(map(int,input().split()))
while True:
    x=input().split()
    if len(x) != 0:
        a2 = list(map(int,x))
        a3 = list(map(int,input().split()))
        break
for i in a3:
    a2.append(i)
    print(max(a2),end=' ')
