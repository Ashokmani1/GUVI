w1=int(input())
s=0
m=len(str(w1))
while w1>0:
    a=int(w1)%10
    s=s+(a**m)
    w1=w1//10
print(s)
