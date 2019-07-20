N1=input()

k=""

m=0

for i in range(len(N1)-1):

    k=""
    
    if N1[i]==N1[i+1]:
    
        k=k+N1[:i+1]+N1[i+2:]
        
        if int(k)>m:
        
            m=int(k)
            
print(m)
