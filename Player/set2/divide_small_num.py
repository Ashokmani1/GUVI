def gcd(a,b): 
    if (a == b): 
        return a 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

a2 = list(map(int,input().split()))
a = a2[0]
b = a2[1]
print(int(lcm(a, b)))
