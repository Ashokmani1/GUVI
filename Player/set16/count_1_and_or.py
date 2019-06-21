a2 = list(map(int,input().split()))
sum = bin(int(bin(a2[0])[2:],2) + int(bin(a2[1])[2:],2))
print(sum[2:].count('1'))
