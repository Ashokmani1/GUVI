1
def gcd(a,b): 
  
    if (a == b): 
        return a 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

a1 = list(map(int,input().split()))
print(int(lcm(a1[0],a1[1])))
