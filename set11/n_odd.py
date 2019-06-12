a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
l=[]
for i in range(0,len(a3)):
    if a3[i]%2 !=0:
        l.append(a3[i])
print(l[a2[1]-1])
