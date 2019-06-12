def sumOfAP( a, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
      
a2=list(map(int,input().split()))
n = a2[2]
a = a2[0]
d = a2[1]
print (sumOfAP(a, d, n)) 
