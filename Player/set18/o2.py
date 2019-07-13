n1,k1=map(int,input().split())
o=list(bin(n1^k1))
print(o.count("1"))
