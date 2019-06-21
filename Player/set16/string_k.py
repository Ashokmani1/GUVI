a1 = input().split()
for i in range(0,len(a1[0]),int(a1[1])):
    print(a1[0][int(a1[1])+i-1],end=' ')
