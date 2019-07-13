a1 = int(input())
b1 = list(map(int,input().split()))
for j in b1:
    if b1.count(j)==1:
        print(j)
        break
