n,k=map(int,input().split())

l1=[int(x) for x in input().split()]

s=0

for i in range(0,len(l1)):

    for j in range(i+1,len(l1)):
    
        if abs(l1[i]-l1[j])==k:
        
            s+=1
            
print(s)
