p=input()
ll=[]
for i in range(0,len(p)):
    for j in range(i+2,len(p)+1):
        aa1=p[i:j]
        if aa1==aa1[::-1]:
            ll.append(aa1)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
