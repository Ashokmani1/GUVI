num1=input()
arr=[]
count=0
for i in range(0,len(num1)-1):
    sum=int(num1[i])+int(num1[i+1])
    if sum%2!=0:
        count+=1
    else:
        arr.append(count)
        count=0
    arr.append(count)
m=max(arr)
if m==0:
    print(0)
else:
    print(m+1)
