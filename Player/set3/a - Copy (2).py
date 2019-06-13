def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 

a2 = list(map(int,input().split()))
print (hcfnaive(a2[0],a2[1])) 
