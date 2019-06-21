a2 = list(map(int,input().split()))
a2 = a2[0] * a2[1]
a3 = list(bin(a2)[2:])

print(a3.count('1'))
