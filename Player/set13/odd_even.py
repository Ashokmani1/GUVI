kk1=int(input())
aa=list(map(int,input().split()))
b=1
for i in aa:
    b=b*i
if b%2==0:
    print("even")
else:
    print("odd")
