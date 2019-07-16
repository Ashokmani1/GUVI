n=int(input())
num=list(map(int,input().split()))
l1=[]
for i in num:
    if num.count(i)>1:
        if str(i) not in l1:
            l1.append(str(i))
if len(l1)==0:
    print("unique")
else:
    num.sort()
    print(" ".join(l1))
