num=int(input())
arr1=list(map(int,input().split()))
sum=0
for i in arr1:
    if i<0:
        sum=sum+i
print(sum)
