a1=int(input())
lis1=list(map(int,input().split()))
for i in lis1:
    if lis1.count(i)>1:
        print(i)
        break
else:
    print("unique")
