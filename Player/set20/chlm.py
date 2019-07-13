p1=int(input())
q1=list(map(int,input().split()))
c=1
for i in range(0,p1-2,2):
    if q1[i]<q1[i+1] and q1[i+1]>q1[i+2]:
        c=c+2
    elif q1[i]>q1[i+1] and q1[i+1]<q1[i+2]:
        c=c+2
    else:
        break
if c==p1:
    print("yes")
else:
    print("no")

