import sys,string
def dgtSum(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

n = int(input())
if n <= 9:
    print(n)
    sys.exit()
a1 = n // 9
b1 = n % 9
if b1 :
    s = str(b1) + str('9') * a1
else :
    s = str('9') * a1
print(s)
