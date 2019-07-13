num1=int(input())
arr1=[list(map(int,input().split(" "))) for i in range(num1)]
i,j=0,len(arr1)-1
a,b=1,1
while i<len(arr1):
    a*=arr1[i][i]
    b*=arr1[i][j]
    i+=1
    j-=1
print(a+b)
