import math
def isprime(x1):
    if(x1 ==2):
        return True
    elif(x1%2 == 0):
        return False
    else:
        for j in range(2,int(math.sqrt(x1)+1)):
            if(x1%j == 0):
                return False
        return True
n = int(input(""))
prime = []
for i in range(2,n):
    if(isprime(i)):
        prime.append(i)
if(len(prime)>0):
    if(prime[-1] == 97):
        print(" ".join(map(str,prime)),"")
    else:
        print(" ".join(map(str,prime)))
else:
    print(0)
