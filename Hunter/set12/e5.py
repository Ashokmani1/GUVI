def PSUM(n1) :
    sum1 = 0
    while n1 :
        sum1 += n1%10
        n1 //= 10
    return sum1

def isPrime(n1) :
    if n1==1 : return False
    if n1==2 or n1==3 : return True
    for i in range(2,n1) :
        if n1%i == 0 :
            return False
    return True

a,b = input().split()
a,b = int(a),int(b)
out = 0
for i in range(a,b+1) :
    sum1 = PSUM(i)
    if isPrime(sum1) :
        out += 1
        
print(out)
