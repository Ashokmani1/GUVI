
def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 


a1=list(map(int,input().split()))
print (hcfnaive(a1[1],a1[0])) 
