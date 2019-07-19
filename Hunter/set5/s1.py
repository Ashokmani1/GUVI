n = int(input()) 

P1 = list(map(int,input().split()))

j = 1

miner = sum(P1)

ind = 0

while(j<n):

    x = sum(P1[:j])
    
    y = sum(P1[j:])
    
    if(x>y):
    
        res=x-y
        
    else:
    
        res=y-x
        
    if(res<miner):
    
       miner = res
       
       ind = n-j
       
       t1 = j
       
      
    j+=1
    
print(t1-ind)
