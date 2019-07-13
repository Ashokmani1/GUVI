n1=list(map(str,input().split()))
for i in range(0,len(n1)):
    d=list(n1[i])
    d=sorted(d)
    n1[i]="".join(d)
print(*n1)
