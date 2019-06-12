a1=list(input())
if len(a1)%2==0:
    a1[int(len(a1)/2)] ='*'
    a1[int(len(a1)/2)-1]='*'
print(a1)
