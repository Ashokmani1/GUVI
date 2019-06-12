a2 =int(input())
a3=list(map(int,input().split()))
a4 = a3[:]
a4.sort()
for i in range(0,len(a3)):
    if a3[i] != a4[i]:
        print(i)
        break
