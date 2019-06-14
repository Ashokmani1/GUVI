a1= int(input())
a2 = list(map(int,input().split()))
x=a2[0]
for i in range(1,len(a2)):
    x= x & a2[i]
print(x)
