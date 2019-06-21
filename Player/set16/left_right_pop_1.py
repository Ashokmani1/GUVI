a2 = list(map(int,input().split()))
a2 = a2[0] * a2[1]
a3 = list(bin(a2)[2:])
a3.pop(a3.index('1'))
print(a3.index('1')+2)
