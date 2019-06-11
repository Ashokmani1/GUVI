def sumOfAP( a, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
      
a1=list(map(int,input().split()))
n = a1[0]
a = a1[1]
d = a1[2]
print (sumOfAP(a, d, n)) 
