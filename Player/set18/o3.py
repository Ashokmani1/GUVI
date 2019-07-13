import sys
n1=list(map(int,input()))
s1=0
n1=n1[::-1]
for i in range(0,len(n1)):
    s1=s1+(n1[i]*(2**i))
for i in range(0,s1+100):
    if 2**i==s1:
        print(2**(i-1))
        sys.exit()
    elif 2**i>s1:
        print(2**i)
        sys.exit()
