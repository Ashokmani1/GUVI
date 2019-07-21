p1=input()
ll=[]
for i in range(0,len(p1)):
    for j in range(i+2,len(p1)+1):
        aa=p1[i:j]
        if aa==aa[::-1]:
            ll.append(aa)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
