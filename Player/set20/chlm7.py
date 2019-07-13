s1=str(input())
n=len(s1)
c1=0
for i in range(0,n//2):
    if s1[i]!=s1[n-i-1]:
        c1=c1+1
if c1<=1:
    print("yes")
else:
    print("no")
