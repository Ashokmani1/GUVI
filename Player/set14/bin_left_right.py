a1 = int(input())
a2 = bin(a1)[2:]
a2 = a2[::-1]
print(a2.index('1')+1)
