a2= int(input())
a3 = list(map(int,input().split()))
x=a3[0]
for i in range(1,len(a3)):
    x= x | a3[i]
print(x)
